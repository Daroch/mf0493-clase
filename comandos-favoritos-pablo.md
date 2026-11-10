# Comandos Favoritos de Linux - Pablo Andrés García Betancourth

Aquí recojo una selección de comandos de terminal de Linux esenciales, junto con una breve descripción de lo que hacen y su nivel de precaución.

1. **`sudo rm -rf`**
- **Descripción:** Borra de forma recursiva y forzosa todos los archivos y carpetas que le indiques sin pedir confirmación.
- **Peligro:** Extremo. Si se ejecuta por descuido en la raíz (`/`), destruye todo el sistema operativo.

2. **`chmod 777`**
- **Descripción:** Cambia los permisos de un archivo o directorio otorgando lectura, escritura y ejecución absoluta a cualquier usuario del sistema.
- **Peligro:** Alto a nivel de seguridad, ya que abre la puerta a que cualquiera modifique o ejecute dichos archivos.

3. **`dd if=/dev/zero of=/dev/sda bs=4M status=progress`**
- **Descripción:** Sobrescribe por completo un disco o partición con ceros a nivel de bloques.
- **Peligro:** Crítico. Destruye de forma irreversible todos los datos del disco de destino.

4. **`(:() { :|:& }; :)`**
- **Descripción:** La famosa "bomba lógica" o *fork bomb*. Crea procesos en bucle de manera exponencial de forma instantánea.
- **Peligro:** Crítico. Congela y colapsa la memoria RAM y el procesador del sistema en cuestión de segundos, obligando a reiniciar la máquina por fuerza bruta.

5. **`iptables -F`**
- **Descripción:** Limpia y borra todas las reglas actuales del cortafuegos (*firewall*) de Netfilter/iptables.
- **Peligro:** Medio/Alto. Deja el equipo completamente desprotegido frente a conexiones de red externas si no hay otras capas de seguridad activas.
