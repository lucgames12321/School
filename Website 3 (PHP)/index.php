<!DOCTYPE html>
<html>
  <head>
    <title>Pantoffels pipo</title>
    <link rel="icon" href="img/favicon.png">
    <link rel="stylesheet" href="css/stylesheet.css" type="text/css" />
  </head>

  <body>

    <div id="container">


      <header>
        <h1 class="krxken">KrxKen he</h1>
        <div id="logo">
          <img class="Logo" src="img/logo.png" alt="Logo">
        </div>
      </header>


      <section>

        <nav>
          <ul>
            <li><a class="navigatie" href="index.php?page=1"><strong> Home </strong></a></li>
            <li><a class="navigatie" href="index.php?page=2"><strong> Over mij </strong></a></li>
            <li><a class="navigatie" href="index.php?page=3"><strong> Eendag </strong></a></li>
            <li><a class="navigatie" href="index.php?page=4"><strong> Opdrachten </strong></a></li>
            <li><a class="navigatie" href="index.php?page=5"><strong> Ontwerp </strong></a></li>
            <li><a class="navigatie" href="files/website1/index.html"><strong> Oude Website </strong></a></li>
            </ul>
        </nav>

        <article>
          <?php
            if (isset( $_GET["page"])) {
                $nummer = $_GET["page"];
            }
            else {
              $nummer = 1;
            }

            switch ($nummer) {

              case 1:
                readfile("home.inc");
                break;

              case 2:
                readfile("overmij.inc");
                break;

              case 3:
                readfile("eendag.inc");
                break;

              case 4:
                readfile("opdrachten.inc");
                break;

              case 5:
                readfile("ontwerp.inc");
                break;

              case 6:
                readfile("logohuis.inc");
                break;

              default:
                readfile("home.inc");
              };
            ?>
        </article>

      </section>


      <footer>
        © 2020-2021 De enige echte Pantoffels!
        <a class="mail" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><strong>Contact<strong></a>
      </footer>

    </div>



  </body>
</html>
