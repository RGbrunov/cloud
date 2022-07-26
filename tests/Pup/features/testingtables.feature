# Created by salome.quispe at 5/26/2022
Feature: Busqueda en google
  Como usuario web, quiero buscar en google para poder responder mis dudas
  # Enter feature description here

  Scenario Outline: Busqueda simple en Google
    Given un navegar web en la pagina de Google
    When se introduce la palabre de busqueda "<frase>"
    Then se muestra  el resultado de la frase "<frase>"
    And los resultados relacionados "<relacionado>"

    Examples: Animales
      | frase    | relacionado       |
      | oso      | oso pardo         |
      | panda    | gigante           |
      | gato     | gato montes       |
      | elefante | elefante africano |
