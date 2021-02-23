// const markHeight = 1.69
// const markWeight = 78

// const johnHeight = 1.95
// const johnWeight = 92

// const markBMI = markWeight/(markHeight**2)
// const johnBMI = johnWeight/(johnHeight**2)

// const markHigerBMI = markBMI > johnBMI

// console.log(markHigerBMI)        //Day1

// const markHeight = 1.88
// const markWeight = 95

// const johnHeight = 1.76
// const johnWeight = 85

// const markBMI = markWeight/(markHeight**2)
// const johnBMI = johnWeight/(johnHeight**2)

// const markHigerBMI = markBMI > johnBMI

// console.log(markHigerBMI)       //Day2

// const markHeight = 1.69
// const markWeight = 78

// const johnHeight = 1.95
// const johnWeight = 92

// const markBMI = markWeight/(markHeight**2)
// const johnBMI = johnWeight/(johnHeight**2)

// const compressionBMI = markBMI > johnBMI

// if(compressionBMI){
//     console.log(`Mark's(${markBMI}) BMI is higer than John's(${johnBMI})`);
// }
// else{
//     console.log(`John's(${johnBMI}) BMI is higer than Mark's(${markBMI})`);
// }

// let dolphinSC = 0, koalaSC = 0;

// for(let i=0; i<3; i++){
//     dolphinSC += prompt("Dolphins Score");
//     koalaSC += prompt("Koalas Score");
// }

// let dolphinAVG = dolphinSC / 3;
// let koalaAVG = koalaSC / 3;

// if(dolphinAVG > koalaAVG){
//     console.log("Dolphins team is win!!");
// }
// else if(dolphinAVG < koalaAVG){
//     console.log("Koalas team is win!!");
// }
// else{
//     console.log("Dolphins team and Koalas team is draw!!");
// }

let bill = prompt("Enter the bill");

let tip = bill >= 50 && bill <= 300 ? bill*0.15 : bill*0.2;

console.log(`The bill was ${bill}, the tip was ${tip}, and the total value ${Number(bill)+Number(tip)}`);