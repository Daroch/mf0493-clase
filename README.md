# MF0493 · Repositorio de clase

Cada alumno añade su ficha en `alumnos/` con una pull request. Al fusionarla, GitHub Actions publica la web con todas las fichas.

1. `git switch -c alumno/tunombre`
2. `cp alumnos/_plantilla.md alumnos/tunombre.md` y rellenarla
3. Commit, `git push -u origin alumno/tunombre` y abrir la pull request

`main` está protegida: solo se cambia con pull requests.
