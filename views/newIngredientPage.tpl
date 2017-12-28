<!DOCTYPE html>
<html>
    <head>
    	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    	<!-- <meta http-equiv="X-UA-Compatible" content="IE=edge"> -->
    	<title>Nová surovina</title>
        % include('bootstrap.tpl')
        % include('styleBody.tpl')
    </head>
    <body>
        % include('navbar.tpl')
        <form id="newIngredientForm" method="POST" action="/newIngredient" class="form-group col-sm-4" accept-charset="UTF-8">

            <label for="name">Název suroviny</label>
            <input type="text" name="name" class="form-control"  required value={{name}}>
            <label for="sugar">Množství sacharidů / 100 g</label>
            <input type="number" name="sugar" class="form-control" step="0.01" required value={{sugar}}>
            <label for="fat">Množství tuku / 100 g</label>
            <input type="number" name="fat" class="form-control" step="0.01" required value={{fat}}>
            <label for="protein">Množství bílkovin / 100 g</label>
            <input type="number" name="protein" class="form-control" step="0.01" required value={{protein}}><br>
            <input id="ajaxButton" type="submit" class="btn btn-primary" value="Přidat surovinu" /><br>
            <span id=genProblem class="problem">{{problem}}</span>
        </form>
    </body>
</html>

        