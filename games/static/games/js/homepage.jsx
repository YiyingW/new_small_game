function Cell(props){
	return (
		<div>
			<a className="btn" href={props.game_id}>{props.game_name}</a>
		</div>
	)
}

function Board(props){
	var cells = []
	for(let i = 0;  i < props.cells.length; i++){
		cells.push(<Cell game_id = {i} game_name={props.cells[i]} handleClick = {props.handleClick} />)
	}
	return (
		<div>
			{cells}
		</div>
	)
}


class Menu extends React.Component {
	constructor(props){
		super(props)
	}
	render(){
		return (
			<div>
				<h1>Choose a game to play:</h1>
				<Board cells = {["connect4game", "number game", "where are you"]}/>
			</div>
		)
	}
}


ReactDOM.render(
	<Menu/>,
	document.getElementById("root")
)