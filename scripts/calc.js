function getSelectedOption() 
{
    var dropdown = document.getElementById("which_food_outlet");
    var selectedOption = dropdown.options[dropdown.selectedIndex].value;
    // console.log(selectedOption); 
    // console.log(dropdown.selectedIndex)

    var frequency = document.getElementById("often").value;
    // console.log(frequency); 

    var emissions = [621, 500, 400, 2000, 1000];
    
    var selectedEmission = emissions[dropdown.selectedIndex];
    var year_total = Math.round(frequency*52*selectedEmission/1000);
    var t1 = "The total emissions in a year is equal to ";
    var para1 = document.getElementById("1");
    para1.textContent = t1.concat(String(year_total)).concat(" kilograms");

    var distance = Math.round(year_total/2.392);
    var t2 = "That's equivalent of driving an average petrol car for ";
    var para2 = document.getElementById("2");
    para2.textContent = t2.concat(String(distance)).concat(" kilometers.");
    var image1 = document.getElementById("carimage");
    image1.classList.remove("car");

    var trees = Math.round(year_total/22);
    var t3 = " trees would be required to absorb the emissions."
    var para3 = document.getElementById("3");
    para3.textContent = String(trees).concat(t3);
    var image2 = document.getElementById("treeimage");
    image2.classList.remove("tree");
}   
