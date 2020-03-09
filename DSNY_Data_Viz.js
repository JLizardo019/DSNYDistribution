/* Julie Lizardo*/

let file;

let pos =0;


// [0 # of recycling bins, 1 #avg distance , 2 site types], [0 # of trash bins, 1 #avg distance , 2 site types], [tons of waste]
let bronx =[];
let brooklyn =[];
let manhattan=[];
let queens = [];
let staten =[];

let state =[];

let bx,bk,qn, si, man, ny, b;

let trash;

function preload()
{
  file = loadStrings('Results.txt');
  // bx = loadImage("Images/Bronx.png");
  // bk = loadImage("Images/Brooklyn.png");
  // man = loadImage("Images/Manhattan.png");
  // qn = loadImage("Images/Queens.png");
  // si = loadImage("Images/Staten Island.png");
  ny = loadImage("Images/New York State.png");
  b = loadImage("Images/Boroughs.png");
  // Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
  trash= loadImage("Images/garbage.png")
}

function setup() {
  createCanvas(1440,900);

  for (let i =0; i<file.length; i++)
  {

    let stat = split(file[i], "\t");

     if (stat[0] == "Brooklyn")
     {
       brooklyn = stat;
     }
   else if (stat[0] == "Bronx")
   {
     bronx = stat;
   }
   else if (stat[0] == "Queens")
   {
     queen =stat;
   }
   else if(stat[0] == "Staten Island")
   {
     staten = stat;
   }

   else if (stat[0] == "Manhattan")
   {
     manhattan = stat;
   }

  }
}

function draw() {
  background(220);

  if (pos>=10000)
  {
    pos=600;
  }
  imageMode(CENTER);
  image(ny, width/2, height/2,width/2.5,height/1.75);

  if (pos>500 && pos<=1500)
  {


    tint(255,map(pos, 0,1000, 0,255));
    image(b, width/2, height/2,width/2.5,height/1.75);
  }
  if (pos>1500 && pos<=2500) // look back at this
  {
    tint(255,map(pos, 0,1000, 0,255));
    image(b, width/2, height/2,width/2.5,height/1.75);
  }

}

function mouseWheel()
{
  pos += event.delta;
}

function scrollDown(){

  textSize(18);
  textFont("Helvetica");
  fill(255);
  text("SCROLL", 22, 130);
  text("DOWN", 22, 150);
  text("↓", 22, 170);
}
