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
