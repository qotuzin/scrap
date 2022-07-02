const carCanvas=document.getElementById("carCanvas");
carCanvas.width=300;
const networkCanvas=document.getElementById("networkCanvas");
networkCanvas.width=500;

const carCtx = carCanvas.getContext("2d");
const networkCtx = networkCanvas.getContext("2d");

const road=new Road(carCanvas.width/2,carCanvas.width*0.9,5);
// Generate AI cars
const N=1000;
const cars=generateCars(N);
let bestCar=cars[0];
if(localStorage.getItem("bestBrain")){
    for(let i=0;i<cars.length;i++){
    cars[i].brain=JSON.parse(
        localStorage.getItem("bestBrain"));
    if(i!=0){
            NeuralNetwork.mutate(cars[i].brain,0.001);
        }
    }
}
// Generate traffic dummy cars
const traffic=[
    //First row of traffic
    new Car(road.getLaneCenter(0),400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),400,30,50,"DUMMY",1),
    //Second row of traffic
    new Car(road.getLaneCenter(0),200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(1),200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),200,30,50,"DUMMY",1),
    //Third row of traffic
    new Car(road.getLaneCenter(1),000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),000,30,50,"DUMMY",1),
    //Fourth row of traffic
    new Car(road.getLaneCenter(0),-200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(1),-200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),-200,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),-200,30,50,"DUMMY",1),
    //Fifth row of traffic
    new Car(road.getLaneCenter(1),-400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),-400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),-400,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),-400,30,50,"DUMMY",1),
    //Sixth row of traffic
    new Car(road.getLaneCenter(0),-600,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(1),-600,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),-600,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),-600,30,50,"DUMMY",1),
    //Seventh row of traffic
    new Car(road.getLaneCenter(1),-800,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),-800,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),-800,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(4),-800,30,50,"DUMMY",1),
    //Eighth row of traffic
    new Car(road.getLaneCenter(0),-1000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(1),-1000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(2),-1000,30,50,"DUMMY",1),
    new Car(road.getLaneCenter(3),-1000,30,50,"DUMMY",1),
];

animate();

//Saves the best performing brain
function save(){
    localStorage.setItem("bestBrain",
        JSON.stringify(bestCar.brain));
}

//Discards the saved brain
function discard(){
    localStorage.removeItem("bestBrain");
}

function generateCars(N){
    const cars=[];
    for(let i=1;i<N;i++){
        cars.push(new Car(road.getLaneCenter(2),600,30,50,"AI"));
    }
    return cars;
}

function animate(time) {
    for(let i=0;i<traffic.length;i++){
        traffic[i].update(road.borders,[]);
    }
    for(let i=0;i<cars.length;i++){
        cars[i].update(road.borders,traffic);
    }
    bestCar=cars.find(
        c=>c.y==Math.min(
            ...cars.map(c=>c.y)
    ));

    carCanvas.height=window.innerHeight;
    networkCanvas.height=window.innerHeight;

    carCtx.save();
    carCtx.translate(0,-bestCar.y+carCanvas.height*0.7);

    road.draw(carCtx);
    for(let i=0;i<traffic.length;i++){
        traffic[i].draw(carCtx,"red");
    }

    carCtx.globalAlpha=0.2;
    for(let i=0;i<cars.length;i++){
        cars[i].draw(carCtx,"blue");
    }
    carCtx.globalAlpha=1;
    bestCar.draw(carCtx,"blue",true);

    carCtx.restore();

    networkCtx.lineDashOffset=-time/100;
    Visualiser.drawNetwork(networkCtx,bestCar.brain);
    requestAnimationFrame(animate);
}
