/*     let aa="aaa"
    let a =()=>console.log("sssss"+this.aa)
    a()
    let b=function ahmad(){console.log("ss")+this.aa }()
 */
class p{
    constructor(name){
        this.name=name
    }
    pA(){
        setTimeout(()=>{
            console.log("A"+this.name)
        },100)
    }
    PF(){ 
        setTimeout((function(){
        console.log("f  "+this.name)
    }).bind(this),100)
  }
}
let ps=new p("ahmad");
ps.pA();
ps.PF();