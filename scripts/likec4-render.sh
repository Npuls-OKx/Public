#!/usr/bin/env bash
# Rendert de LikeC4-views van een pakket naar PNG, ingedeeld per categorie.
#
#   scripts/likec4-render.sh <modelmap> <beeldmap>
#   scripts/likec4-render.sh Koppelvlakspecificaties/model Koppelvlakspecificaties/src/diagrammen
#
# De stappen: valideren, de berekende afmetingen als JSON ophalen, de plaatsing
# van de views zonder relaties herberekenen, renderen, en de platen in een map
# per categorie zetten. Die indeling komt uit de titel van de view, dus uit het
# model; zie scripts/likec4-plaatsen.py.
#
# Drie rondes renderen, waarbij een latere ronde overschrijft wat anders moet.
# Een uitsluitende filter (`!naam`) bleek niet te werken, dus wordt er eerst
# alles gerenderd. De dynamische views komen als sequentiediagram, want die
# leest als stap-voor-stap het beste. De situatieplaten krijgen geen legenda:
# daar draagt de kleur de betekenis in plaats van de elementsoort.
#
# De snapshots in <modelmap>/.likec4/ bestaan alleen tijdens deze rit.
set -euo pipefail

if [ $# -lt 2 ]; then
  sed -n '2,8p' "$0" >&2
  exit 2
fi

modelmap="$1"
beeldmap="$2"

rm -rf "${modelmap}/.likec4" likec4.json
npx --yes likec4 validate "$modelmap"
npx --yes likec4 export json "$modelmap"
python3 scripts/likec4-layout.py "$modelmap"

tijdelijk="$(mktemp -d)"
trap 'rm -rf "$tijdelijk" "${modelmap}/.likec4"' EXIT

npx --yes likec4 export png "$modelmap" --output "$tijdelijk" --theme light --flat --notation
npx --yes likec4 export png "$modelmap" --output "$tijdelijk" --theme light --flat --notation --seq \
  --filter 'release_*' --filter 'adoptie_*' --filter 'volgorde_*'
npx --yes likec4 export png "$modelmap" --output "$tijdelijk" --theme light --flat \
  --filter 'afnemer_blijft' --filter 'aanbieder_achter' --filter 'derde_major' \
  --filter 'reikwijdte' --filter 'staalkaart_*' --filter 'pad_*' --filter 'versielagen'

python3 scripts/likec4-marge.py "$tijdelijk"
python3 scripts/likec4-plaatsen.py "$tijdelijk" "$beeldmap"
rm -f likec4.json
