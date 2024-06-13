"use strict";

document.addEventListener("DOMContentLoaded", async () => {
    const baseUrl = "http://localhost:8000";

    const response = await fetch(`${baseUrl}`);
    const shelters = await response.json();

    shelters.sort((a, b) => a.name.localeCompare(b.name));

    const contentElement = document.getElementById("shelters");

    for (let i = 0; i < shelters.length; i++) {
        const shelterElement = createShelterElement(shelters[i]);
        contentElement.appendChild(shelterElement);
    }

});

function createShelterElement(shelter) {
    const section = document.createElement("section");
    section.className = "shelter-card";

    const addressParts = shelter.address.split(", ");
    const street = addressParts[0];
    const cityStateZip = addressParts.slice(1).join(", ");

    section.innerHTML = `
            <h3>${shelter.name}</h3>
            <address>${street}<br>${cityStateZip}</address>
            <p>Dogs: ${shelter.animals.dogs}</p>
            <p>Cats: ${shelter.animals.cats}</p>`;
    return section;
};