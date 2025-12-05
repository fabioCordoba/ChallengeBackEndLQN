### Obtener lista de Planetas:

```graphql
query {
  allPlanets {
    id
    name
    climate
    terrain
    population
  }
}
```

### Obtener un planeta por ID:

```graphql
query {
  planetById(id: "eaa16825-1b22-41d9-a4bd-924491ffc8b3") {
    id
    name
    climate
    isActive
    population
    terrain
    createdAt
    updatedAt
  }
}
```

### Crear un planeta:

```graphql
mutation MyMutation {
  createPlanet(
    name: "planet 0"
    climate: "temperate"
    population: "2000000000"
    terrain: "grassy hills, swamps"
  ) {
    planet {
      climate
      name
      population
      terrain
      updatedAt
      isActive
    }
  }
}
```

### Obtener lista de Peliculas:

```graphql
query {
  allFilms {
    id
    title
    episodeId
    openingCrawl
    director
    producers
    releaseDate
    planets {
      edges {
        node {
          name
        }
      }
    }
  }
}
```

### Obtener peliculas por ID:

```graphql
query {
  filmById(id: "027ddf5c-5000-48e7-9d56-27d797ef82c2") {
    id
    title
    releaseDate
    director
    createdAt
    episodeId
    isActive
    openingCrawl
    producers
  }
}
```

### Crear una pelicula:

```graphql
mutation MyMutation {
  createFilm(
    title: "film 0"
    director: "directoir test"
    openingCrawl: "lorem ..."
    producers: "producers test"
    releaseDate: "1977-05-25"
    planetIds: [
      "eaa16825-1b22-41d9-a4bd-924491ffc8b3"
      "6abc595d-7dfe-4861-b12d-01e5dccd6fe1"
    ]
  ) {
    film {
      isActive
      openingCrawl
      director
      createdAt
      episodeId
      producers
      releaseDate
      title
      planets {
        edges {
          node {
            name
          }
        }
      }
    }
  }
}
```

### Obtener lista de personajes:

```graphql
query {
  allCharacters {
    id
    name
    birthYear
    gender
    height
    mass
    homeworld {
      name
    }
    films {
      edges {
        node {
          title
        }
      }
    }
  }
}
```

### Obtener un personaje por ID:

```graphql
query {
  characterById(id: "cb4b6ce0-01f8-4650-af6f-bc31bbe62386") {
    id
    name
    homeworld {
      name
    }
    films {
      edges {
        node {
          title
        }
      }
    }
  }
}
```

### Filtrar personajes por nombre:

```graphql
query {
  characters(name: "luk", first: 10) {
    edges {
      node {
        id
        name
        birthYear
      }
    }
  }
}
```

### Crear un personaje:

```graphql
mutation MyMutation {
  createCharacter(
    name: "Person"
    birthYear: "19BBY"
    gender: "male"
    height: "170"
    mass: "80"
    homeworldId: "eaa16825-1b22-41d9-a4bd-924491ffc8b3"
    filmIds: ["027ddf5c-5000-48e7-9d56-27d797ef82c2"]
  ) {
    character {
      id
      name
      birthYear
      gender
      height
      mass
      homeworld {
        id
        name
      }
      createdAt
      isActive
    }
  }
}
```
