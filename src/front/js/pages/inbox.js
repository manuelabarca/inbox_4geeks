import React, {useEffect, useContext} from "react";
import {Context} from "../store/appContext";

const Inbox = () => {

	const {store, actions} = useContext(Context);

	useEffect(() => {

		actions.getMessages()

	}, [store.inbox])

	return (
		<div className="container">
			<div className="row">
				<div className="col-2 person-message">One of three columns</div>
				<div className="col-auto">One of three columns</div>
			</div>
		</div>
	);
};

export default Inbox;
