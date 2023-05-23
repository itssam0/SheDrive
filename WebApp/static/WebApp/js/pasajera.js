// Variables globales
let map;
let directionsService;
let directionsRenderer;
let originInput;
let destinationInput;
let distanceElement;

function initMap() {
    const localPredec = { lat: 6.217, lng: -75.567 };
    map = new google.maps.Map(document.getElementById("map"), {
    center: localPredec,
    zoom: 11,
});

  // Inicializar el servicio de direcciones y el renderizador de direcciones
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

  // Obtener referencias a los elementos de entrada
    originInput = document.getElementById("origin-input");
    destinationInput = document.getElementById("destination-input");
    distanceElement = document.getElementById("distance");

  // Escuchar el evento de envío del formulario para obtener la ruta
    document.getElementById("directions-form").addEventListener("submit", calculateRoute);
}

function calculateRoute(event) {
    event.preventDefault();

  // Obtener los valores de origen y destino desde los inputs
    const origin = originInput.value;
    const destination = destinationInput.value;

  // Realizar la solicitud de ruta al servicio de direcciones de Google Maps
    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING,
    },
    (response, status) => {
        if (status === "OK") {
            // Mostrar la ruta en el mapa
            directionsRenderer.setDirections(response);

            // Obtener el tiempo estimado, la distancia y la duración de la ruta
            const route = response.routes[0];
            if (route && route.legs && route.legs.length > 0) {
                const duration = route.legs[0].duration.text;
                const distance = route.legs[0].distance.text;

                const durationElement = document.getElementById("duration");
                durationElement.textContent = `Tiempo estimado: ${duration}`;
                
              // Mostrar la distancia en la página
                const distanceElement = document.getElementById("distance");
                distanceElement.textContent = `Distancia: ${distance}`;

                const distanceValue = route.legs[0].distance.value;
                const fuelEfficiency = 12; // Eficiencia de combustible en km/L 
                const fuelPrice = 5000; // Precio del combustible en la moneda local 
                const fuelCost = ((distanceValue / 1000) / fuelEfficiency * fuelPrice) * 4.5;
                const fuelCostElement = document.getElementById("fuel-cost");
                fuelCostElement.textContent = `Costo estimado: $${fuelCost.toFixed(2)}`;

              // Actualizar los campos ocultos con los valores correspondientes
                const distanceInput = document.getElementById("distance-input");
                const priceInput = document.getElementById("price-input");
                const durationInput = document.getElementById("duration-input");

                distanceInput.value = distance;
                priceInput.value = fuelCost.toFixed(2);
                durationInput.value = duration;
            }
        } else {
        // Ocurrió un error al calcular la ruta
            Swal.fire({
                title: "Error",
                text: "No se pudo calcular su ruta. Recuerde ingresar la ciudad y el país del origen y del destino",
                icon: "error",
                showCloseButton: "true",
            });
        }
    }
);
}

function notificacion(){
    Swal.fire({
        "title": "Espera un momento",
        "text": "¡Su viaje ya ha sido solicitado! espera la confirmacion de su viaje",
        "icon": "warning",
        "showCloseButton": "true",
    })
}
