<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/">Ketogenní kalkulačka</a>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".navbar-collapse" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div id="navbarNav" class="collapse navbar-collapse">

        <ul class="nav navbar-nav navbar-center">
          <li class="nav-item">
            <a class="nav-link" href="/user">{{ icons.user }}</a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Přidat
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="/newrecipe">recept</a>
              <a class="dropdown-item" href="/newdiet">dietu</a>
              <a class="dropdown-item" href="/newingredient">surovinu</a>
            </div>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Seznamy
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="/allingredients">Všechny suroviny</a>
              <a class="dropdown-item" href="/alldiets">Všechny diety</a>
              <!-- <div class="dropdown-divider"></div> -->
              <a class="dropdown-item" href="/allrecipes">Všechny recepty</a>
            </div>
          </li>

        </ul>

        <ul class="nav navbar-nav navbar-right ml-auto">

          <li class="nav-item">
            <a class="nav-link small" href="/changelog">Změny</a>
          </li>
          <li class="nav-item">
            <a class="nav-link small" href="/feedback">Připomínky</a>
          </li>
{#           <li class="nav-item">
            <a class="nav-link small" href="/help">Nápověda</a>
          </li> #}
          <li class="nav-item">
            <a class="nav-link" href="/logout">Odhlásit se</a>
          </li>
        </ul>

    </div>

  </div>
</nav>
{% include('flashing.tpl') %}