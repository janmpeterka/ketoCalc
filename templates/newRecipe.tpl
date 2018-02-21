{% extends "base.tpl" %}
{% block title %}
    Nový recept
{% endblock %}

{% block style %}
    <style type="text/css" media="screen">
        .recipe__wrong{
            display: none;
        }

        .recipe__right{
            display: none;
        }

       .container__main {
            margin-top: 40px;
        }

        .recipe__loader {
            display: none;
            border: 16px solid #f3f3f3; /* Light grey */
            border-top: 16px solid #337ab7; /* Blue */
            border-radius: 50%;
            width: 200px;
            height: 200px;
            animation: spin 2s linear infinite;
            margin: 40px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

    </style>
{% endblock %}

{% block script %}
	<script type="text/javascript">

            /// On ready - change visibility to default
            $(document).ready(function() {
                allIngredients = $(".prerecipe__add-ingredient__form__select").html();
                $(".recipe__right").hide();
                $(".recipe__wrong").hide();
                $(".recipe__loader").hide();
                prerecipe__selectedIngredients__table__empty();
                prerecipe__calc__form__empty();
                $('.js-example-basic-single').select2();
            });

            // ingredient select to actual
            function prerecipe__addIngredient__form__select__refresh(){
                $('.prerecipe__add-ingredient__form__select').empty();
                $('.prerecipe__add-ingredient__form__select').append(allIngredients);

                temp_array=$('.prerecipe__calc__form input[name=ingredients]').val().split(", ");
                for (let i = 0; i < temp_array.length; i++) {
                    $('.prerecipe__add-ingredient__form__select option[value="' + temp_array[i] + '"]').remove(); // wip
                }
            }

            // ingredient select to default
            function prerecipe__addIngredient__form__select__renew(){
                $('.prerecipe__add-ingredient__form__select').empty();
                $('.prerecipe__add-ingredient__form__select').append(allIngredients);
            }


            // empty prerecipe ingredients table
            function prerecipe__selectedIngredients__table__empty(){
                $('.prerecipe__selected-ingredients__table').empty();
                $(".prerecipe__selected-ingredients__table").append(
                    '<tr>'+
                        '<th>Název</th>'+
                        '<th>Kalorie</th>'+
                        '<th>Bílkovina</th>'+
                        '<th>Tuk</th>'+
                        '<th>Sacharidy</th>'+
                        '<th>Hlavní?</th>'+
                    '</tr>');
            }

            function prerecipe__selectedIngredients__table__add(ingredient){
                $('.prerecipe__selected-ingredients__table').append(
                "<tr>" + 
                    "<td>" + ingredient.name + "</td>" +
                    "<td>" + ingredient.calorie + "</td>" +
                    "<td>" + ingredient.protein+ "</td>" +
                    "<td>" + ingredient.fat + "</td>"+
                    "<td>" + ingredient.sugar + "</td>"+
                    "<td>" +
                        '<input type="radio" onclick="setMainIngredient('+ ingredient.id +')" class="form-check-input" name="Proměnná"/>' +
                        '<button id="' + ingredient.id + '" class="remove btn btn-warning">Ubrat</button>' +
                    // "</td>"+
                    // "<td>" +
                    "</td>"+
                "</tr>");
            }

            // empty recipe ingredients table
            function recipe__right__form__ingredientTable__empty(){
                $('.recipe__right__form__ingredient-table').empty();
                $('.recipe__right__form__ingredient-table').append(
                    '<tr>'+
                        '<th>Název</th>'+
                        '<th>Kalorie</th>'+
                        '<th>Bílkovina</th>'+
                        '<th>Tuk</th>'+
                        '<th>Sacharidy</th>'+
                        '<th>Množství</th>'+
                        '<th></th>'+
                    '</tr>');
            }

            // add ingredient to recipe
            function recipe__right__form__addIngredient(ingredient){
                var tempVal = $('.recipe__right__form input[name=ingredients]').val();
                if (tempVal.length === 0) {
                    $('.recipe__right__form input[name=ingredients]').val(ingredient.id);
                } else {
                    $('.recipe__right__form input[name=ingredients]').val(tempVal + ", " + ingredient.id);
                }
            }

            // add ingredient amount to recipe
            function recipe__right__form__addAmount(ingredient){
                var tempVal = $('.recipe__right__form input[name=amounts]').val();
                if (tempVal.length === 0) {
                    $('.recipe__right__form input[name=amounts]').val(Math.round(ingredient.amount));
                } else {
                    $('.recipe__right__form input[name=amounts]').val(tempVal + ", " + Math.round(ingredient.amount));
                }
            }

            // empty prerecipe form values
            function prerecipe__calc__form__empty(){
                $('.prerecipe__calc__form input[name=main-ID]').val("");
                $('.prerecipe__calc__form input[name=ingredients]').val("");
            }

            // empty recipe form values
            function recipe__right__form__empty(){
                $('.recipe__right__form input[name=ingredients]').val("");
                $('.recipe__right__form input[name=amounts]').val("");
                $('.recipe__right__form input[name=diet-ID]').val("");
            }

            // remove prerecipe__form ingredient
            function prerecipe__calc__form__ingredients__remove(id){
                var temp_array = $('.prerecipe__calc__form input[name=ingredients]').val().split(", ");
                temp_array.splice($.inArray(id, temp_array),1);

                $('.prerecipe__calc__form input[name=ingredients]').val("");

                for (let i = 0; i < temp_array.length; i++) {
                    prerecipe__calc__form__ingredients__add(temp_array[i]);
                }
            }

            // add prerecipe__form ingredient
            function prerecipe__calc__form__ingredients__add(id){
                var temp_array = $('.prerecipe__calc__form input[name=ingredients]').val();
                if (temp_array.length === 0) {
                    $('.prerecipe__calc__form input[name=ingredients]').val(id);
                } else {
                    $('.prerecipe__calc__form input[name=ingredients]').val(temp_array + ", " + id);
                }
            }
            

            // visibility
            function recipe__loader__show(){
                $(".recipe__loader").show();
                $(".recipe__right").hide();
                $(".recipe__wrong").hide();
            }

            function recipe__wrong__show(){
                $(".recipe__loader").hide();
                $(".recipe__wrong").show();
                $(".recipe__right").hide();
            }

            function recipe__right__show(){
                $(".recipe__loader").hide();
                $(".recipe__wrong").hide();
                $(".recipe__right").show();
            }

            function recipe__hideAll(){
                $(".recipe__loader").hide();
                $(".recipe__wrong").hide();
                $(".recipe__right").hide();
            }


            $(document).on("submit", ".prerecipe__calc__form", function(e) {
                    $.ajax({
                        type: 'POST',
                        url: '/calcRecipeAJAX',
                        data: $(this).serialize(),
                        success: function(response){

                            // // empty form datas
                            // prerecipe__calc__form__empty();
                            recipe__right__form__empty();

                            // // empty tables
                            // prerecipe__selectedIngredients__table__empty();
                            recipe__right__form__ingredientTable__empty();

                            // // renew selection
                            // prerecipe__addIngredient__form__select__renew();

                            if (response=="False"){
                                recipe__wrong__show();
                                return;
                            }

                            var totalCalorie = 0;
                            var totalProtein = 0;
                            var totalFat = 0;
                            var totalSugar = 0;
                            var ingredients = response.ingredients;

                            // ingredients to table
                            for ( let i = 0; i<response.ingredients.length; i++ ){

                                if (response.mainIngredientID == ingredients[i].id){
                                    $('.recipe__right__form__ingredient-table').append(
                                        '<tr>' +
                                        "<td>" + ingredients[i].name + "</td>" +
                                        "<td>" + ingredients[i].calorie + "</td>" +
                                        "<td>" + ingredients[i].protein + "</td>" +
                                        "<td>" + ingredients[i].fat + "</td>" +
                                        "<td>" + ingredients[i].sugar + "</td>" +
                                        '<td><span id="amount_' + ingredients[i].id + '">' + Math.round(ingredients[i].amount)+ " g</span></td>" + 
                                        '</tr>' +

                                        '<tr>' +
                                            '<td id="slider_tr" name="'+ response.mainIngredientID +'" class="row">' + 
                                                '<input type="range"' +
                                                    'class="col"' +
                                                    'id="slider"' + 
                                                    'name="slider"' + 
                                                    'min="' + response.mainIngredientMin + '" '+
                                                    'max="' + response.mainIngredientMax + '" '+
                                                    'step="0.1" '+
                                                    'oninput="showSliderVal(this.value, amount_'+ingredients[i].id + ')" '+
                                                    'onchange="showSliderVal(this.value, amount_'+ingredients[i].id + ')">' +
                                                
                                            '</td>' +

                                            '<td colspan="2">' + 
                                                '<span class="col">' +
                                                    ingredients[i].name +
                                                '</span>' + 
                                            '</td>' + 

                                            '<td colspan="2">' + 
                                                '<span id="sliderVal" class="col"></span>' + 
                                            '</td>' + 
                                        '</tr>'


                                        );

                                }
                                else {
                                    $('.recipe__right__form__ingredient-table').append(
                                        "<tr>" +
                                        "<td>" + ingredients[i].name + "</td>" +
                                        "<td>" + ingredients[i].calorie + "</td>" +
                                        "<td>" + ingredients[i].protein + "</td>" +
                                        "<td>" + ingredients[i].fat + "</td>" +
                                        "<td>" + ingredients[i].sugar + "</td>" +
                                        '<td><span id="amount_' + ingredients[i].id + '">' + Math.round(ingredients[i].amount)+ " g</span></td>" +
                                        "</tr>");
                                }

                                totalCalorie += ingredients[i].calorie*ingredients[i].amount;
                                totalProtein += ingredients[i].protein*ingredients[i].amount;
                                totalFat += ingredients[i].fat*ingredients[i].amount;
                                totalSugar += ingredients[i].sugar*ingredients[i].amount;
                            }

                            $('.recipe__right__form__ingredient-table').append(
                                "<tr>" +
                                    '<td>'+
                                        '<strong>Součet</strong>'+
                                    '</td>'+
                                    '<td>'+
                                        '<span id="totalCalorie">' + 
                                        Math.round(totalCalorie/100) +
                                        '</span>'+
                                    '</td>' + 

                                    '<td>'+
                                        '<span id="totalProtein">' + 
                                        Math.round(totalProtein/100) +
                                        '</span>'+
                                    '</td>' + 
                                    '<td>'+
                                        '<span id="totalFat">' + 
                                        Math.round(totalFat/100) +
                                        '</span>' +
                                    '</td>' + 
                                    '<td>'+
                                        '<span id="totalSugar">' + 
                                        Math.round(totalSugar/100) +
                                        '</span>' +
                                    '</td>' + 
                                '</tr>');

                            // ingredient IDs and amounts to inputs
                            for (let i = 0; i<ingredients.length; i++ ){
                                recipe__right__form__addIngredient(ingredients[i]);
                                recipe__right__form__addAmount(ingredients[i]);
                            }

                            // diet ID
                            $('.recipe__right__form input[name=diet-ID]').val(response.dietID);
                            $('.recipe__right__form__diet-name').text(response.dietName);

                            // change visibility
                            recipe__right__show();

                        },
                        error: function(error) {
                            // console.log(error);
                        }
                    });
                    e.preventDefault();
                });

            /// Adding ingredient from select to list of selected ingredients
            $(document).on("submit", ".prerecipe__add-ingredient__form", function(e) {
                    $.ajax({
                        type: 'POST',
                        url: '/addIngredientAJAX',
                        data: $(this).serialize(),
                        success: function(response) {
                            var ingredient = response;
                            prerecipe__calc__form__ingredients__add(ingredient.id);
                            prerecipe__addIngredient__form__select__refresh();
                            prerecipe__selectedIngredients__table__add(ingredient); // gets data from form__ings
                            recipe__hideAll();
                        },
                        error: function(error) {
                            // console.log(error);
                        }
                    });
                    e.preventDefault();
            });

            /// Removing ingredient from list of selected ingredients
            $(function(){
                  $('.prerecipe__selected-ingredients__table').on('click','tr button.remove',function(e){
                     e.preventDefault();

                    // remove table line
                    $(this).parents('tr').remove();

                    // remove from list
                    prerecipe__calc__form__ingredients__remove($(this).attr('id'));

                    // Refresh selection
                    prerecipe__addIngredient__form__select__refresh();
                  });
            });

            
            /// Running loader animation
            $(document).on("click", ".prerecipe__calc__form__submit", function() {
                recipe__loader__show();
            });
            

            /// Recalculating amounts 
            $(document).on("change", "#slider", function(e) {
                recipe__loader__show();

                var dietID = $('.recipe__right__form input[name=diet-ID]').val();
                var ingredientsArray = $('.recipe__right__form input[name=ingredients]').val();
                var slider = $('#slider').val();
                var mainIngredientID = $('#slider_tr').attr('name');

                $.ajax({
                        type: 'POST',
                        url: '/recalcRecipeAJAX',
                        data: JSON.stringify({'dietID': dietID, 'ingredientsArray': ingredientsArray, 'slider': slider, 'mainID': mainIngredientID}, null, '\t'),
                        contentType: 'application/json;charset=UTF-8',

                        success: function(response) {

                            // new amounts
                            var x = response.x;
                            $('#amount_'+x.id).text(x.amount + " g");
                            var y = response.y;
                            $('#amount_'+y.id).text(y.amount + " g");
                            var z = response.z;
                            $('#amount_'+z.id).text(z.amount + " g");
                            var slider = response.slider;
                            $('#amount_'+ slider.id).text(slider.amount + " g");

                            // new totals 
                            $('#totalFat').text(response.totals.fat);
                            $('#totalSugar').text(response.totals.sugar);
                            $('#totalProtein').text(response.totals.protein);
                            $('#totalCalorie').text(response.totals.calorie);


                            // new amounts in form
                            ingredients = [x, y, z, slider];
                            $('.recipe__right__form input[name=amounts]').val("");
                            for (let i = 0; i < ingredients.length; i++ ){
                                recipe__right__form__addAmount(ingredients[i]);
                            }

                            recipe__right__show();

                        },
                        error: function(error) {
                        }

                    });
                    e.preventDefault();
            });

            function setMainIngredient(id){
                $('.prerecipe__calc__form input[name=main-ID]').val(id);
            }

            function showSliderVal(value){
                $('#sliderVal').text(value);
            }

        </script>
{% endblock %}

{% block content %}
	{% include('navbar.tpl') %}
        <div class="container container__main">
            <div class="row">
                <div class="prerecipe col-lg-6 col-md-12">

                    <div class="prerecipe__add-ingredient col-12">
                        <form class="prerecipe__add-ingredient__form form-inline">
                            <select class="prerecipe__add-ingredient__form__select form-control js-example-basic-single"
                            name="prerecipe__add-ingredient__form__select">
                            {% for ingredient in ingredients: %}
                                <option name={{ingredient.name}} value="{{ingredient.id}}">{{ingredient.name}}</option>
                            {% endfor %}
                            </select>
                            <input type="submit" class="btn btn-primary" value="Přidat surovinu" />
                        </form>
                    </div>
                    
                    <div class="prerecipe__selected-ingredients col-10">
                        <form class="form-group">
                            <table class="prerecipe__selected-ingredients__table table"></table>
                        </form>
                    </div>

                    <div class="prerecipe__calc col-12">
                        <form class="prerecipe__calc__form form-inline">
                            <label for="select-diet">Název diety</label>
                            <select name="select-diet" class="form-control">
                            {% for diet in diets: %}
                                <option value="{{diet.id}}">{{ diet.name }}</option>
                            {% endfor %}
                            </select>
                            <input type="submit" class=" prerecipe__calc__form__submit btn btn-primary" value="Spočítat množství!" />
                            <input type="hidden" name="ingredients" value="" />
                            <input type="hidden" name="main-ID" value="" />
                        </form>
                    </div>

                </div>


                <div class="recipe col-lg-6 col-md-12">

                    <div class="recipe__loader"></div>

                    <div class="recipe__wrong">
                        <span class="problem">Recept nelze vytvořit</span>
                    </div>

                    <div class="recipe__right">
                        <form method="post" class="recipe__right__form form-group"  action="/saveRecipeAJAX" >
                            <label for="recipe__right__form__name-input">Název receptu</label>
                            <input type="text" name="recipe__right__form__name-input" required class="form-control"/>
                            
                            <table class="recipe__right__form__ingredient-table table">
                                <tr>
                                    <th>Název</th>
                                    <th>Kalorie</th>
                                    <th>Bílkovina</th>
                                    <th>Tuk</th>
                                    <th>Sacharidy</th>
                                    <th>Množství</th>
                                    <th></th>
                                </tr>
                            </table>
                            
                            <div class="form-inline">
                                <select name="recipe__right__form__size-select" class="form-control col-3">
                                    <option value="big">Velké jídlo</option>
                                    <option value="small">Malé jídlo</option>
                                </select>

                                <!-- <span class="col-2"></span> -->
                                <span class="col-4">Dieta: <span class="recipe__right__form__diet-name"></span></span>
                                <input type="submit" class="btn btn-primary col-4 " value="Uložit mezi recepty" />
                            </div>
                            
                            <input type="hidden" name="ingredients" value="" />
                            <input type="hidden" name="diet-ID" value="" />
                            <input type="hidden" name="amounts" value="" />
                        </form>
                    </div>
                </div>
            </div>
        </div>    
{% endblock %}

