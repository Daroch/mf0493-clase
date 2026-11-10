#!/usr/bin/env bash
# Comprueba las fichas de alumnos/. Lo ejecuta GitHub Actions en cada pull request.
# Los mensajes ::error aparecen en la PR, junto a la línea del fichero.
errores=0
for f in alumnos/*.md; do
  nombre=$(basename "$f")
  [[ "$nombre" == _* ]] && continue
  antes=$errores

  if [[ ! "$nombre" =~ ^[a-z0-9-]+\.md$ ]]; then
    echo "::error file=$f::El nombre del fichero solo puede tener minúsculas, números y guiones (sin tildes ni espacios)"
    errores=$((errores + 1))
  fi

  if ! head -n 1 "$f" | grep -Eq '^# +[^ ]'; then
    echo "::error file=$f,line=1::La primera línea tiene que ser '# ' seguido de tu nombre"
    errores=$((errores + 1))
  fi

  linea=$(grep -n 'Comando de Linux favorito:' "$f" | head -n 1 | cut -d: -f1)
  if [[ -z "$linea" ]]; then
    echo "::error file=$f::Falta la línea '- Comando de Linux favorito:'"
    errores=$((errores + 1))
  elif ! sed -n "${linea}p" "$f" | grep -Eq 'favorito: *[^ ]'; then
    echo "::error file=$f,line=$linea::El comando favorito está vacío"
    errores=$((errores + 1))
  fi

  [[ $errores -eq $antes ]] && echo "OK  $f"
done

if [[ $errores -gt 0 ]]; then
  echo "$errores error(es). Corrígelos, haz commit y push: la comprobación se repite sola."
  exit 1
fi
echo "Todas las fichas están bien."
