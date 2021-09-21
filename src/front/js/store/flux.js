const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			inbox: [],
			api: 'https://3001-brown-moth-2tivf4or.ws-us15.gitpod.io'
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: () => {
				// fetching data from the backend
				fetch(process.env.BACKEND_URL + "/api/hello")
					.then(resp => resp.json())
					.then(data => setStore({ message: data.message }))
					.catch(error => console.log("Error loading message from backend", error));
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
			getMessages: () => {
				const store = getStore()
				fetch(`${store.api}/api/messages`,{
					method: 'GET',
					headers: {
						'Content-type': 'application/json'
					}
				})
				.then(resp => {
					if(resp.ok){
						return resp.json()
					}
				})
				.then(data => console.log(data))
				.catch(error => console.error("[Error to get inbox]", error))
			}
		}
	};
};

export default getState;
