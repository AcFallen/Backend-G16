const button = document.getElementById("crearProductoBtn");
const nombreProducto = document.getElementById("nombre");
const precioProducto = document.getElementById("precio");
const disponibleProducto = document.getElementById("disponible");

function crearProducto(e) {
  e.preventDefault();
  const body = {
    nombre: nombreProducto.value,
    precio: +precioProducto.value,
    disponible: disponibleProducto.checked,
  };

  crearProductoRequest(body)
    .then((resultado) => {
      if (resultado === true) {
        alert("Producto creado exitosamente");
      } else {
        alert("Error al crear el producto");
      }
    })
    .catch((e) => {
      alert(`Error al crear el producto! ${e.message}`);
    });
}

async function crearProductoRequest(body) {
  const solicitud = await fetch("http://127.0.0.1:5000/producto", {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
    },
  });

  return solicitud.status === 201;
}

button.addEventListener("click", crearProducto);

async function pedirProductos() {
  const solicitud = await fetch("http://127.0.0.1:5000/productos");
  //   console.log(solicitud.status);
  //   console.log(await solicitud.text())
  const data = await solicitud.json();
  console.log(data);
}

pedirProductos();
