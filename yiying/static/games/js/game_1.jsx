function Row(props) {
  return (
    <div>
      <button className="button" onClick = {()=>props.handleClick(props.row_id)}>
        {props.option}
      </button>
    </div>
  )
}

function Board(props) {
  var rows = []
  for (let i=0; i<4; i++){
    rows.push(<Row row_id = {i} option = {props.options[i]} handleClick = {props.handleClick}/>);
  }
  return (
    <div>
      {rows}
    </div>
  )
}

function shuffleArray(array) {
  let i = array.length - 1;
  for (; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}

class Game extends React.Component{
  constructor(props){
    super(props)
    let tmp = this.newQuestion();
    this.state = {question:tmp[0], options:tmp[1], c_ans:tmp[2], i_count:0, c_count:0}
    this.handleClick = this.handleClick.bind(this)
  }


  newQuestion(){
    let left = Math.floor(Math.random() * 20) + 1;
    let right = Math.floor(Math.random() * 20) + 1;
    let op = Math.floor(Math.random() * 3) + 1; //1 + 2 - 3 *
    let c_ans;
    let q_s;
    switch(op) {
      case 1:
        c_ans = left + right
        q_s = left + " + " + right;
        break;
      case 2:
        c_ans = left - right;
        q_s = left + " - " + right;
        break;
      case 3:
        c_ans = left * right;
        q_s = left + " * " + right;
        break;
    }
    let ans = [c_ans];
    while (ans.length < 4){
      let tmp = Math.floor(Math.random() * 20) - 10;
      if (ans.indexOf(tmp) == -1){
        ans.push(tmp);
      }
    }
    shuffleArray(ans);
    return [q_s, ans, c_ans]
  }
  
  checkAns(option_num){
    if (this.state.c_ans == this.state.options[option_num]){
      return 1;
    } else {
      return 0;
    }
  }

  handleClick(option_num){
    //if current option correct, update below:
    // i_count c_count question and options
    let tmp = this.newQuestion();
    let res = this.checkAns(option_num);
    let nex_i_count;
    let nex_c_count;
    if (res == 1){
      nex_i_count = this.state.i_count;
      nex_c_count = this.state.c_count + 1;
    } else {
      nex_i_count = this.state.i_count + 1;
      nex_c_count = this.state.c_count;
    }
    this.setState({question:tmp[0], options:tmp[1], i_count:nex_i_count, c_count:nex_c_count, c_ans:tmp[2]})
  }
  
  restart(){
    let tmp = this.newQuestion();
    this.setState({question:tmp[0], options:tmp[1], i_count:0, c_count:0, c_ans:tmp[2]})
  }

  render(){
    
    return (
      <div>
        <h2 style={{color:"yellow"}}>Question: {this.state.question} ?</h2>
        <Board options = {this.state.options} handleClick = {this.handleClick}/>
        <div className="highlight">
          <h2 style={{color:"green"}}> Correct: {this.state.c_count} </h2>
          <h2 style={{color:"red"}}> Incorrect: {this.state.i_count} </h2>
        </div>
        <button className = "restart_button" onClick = {()=> this.restart()}>Restart</button>
      </div>
    )
  }
}

ReactDOM.render(
  <Game/>,
  document.getElementById("root")
)