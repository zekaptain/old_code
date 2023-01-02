using UnityEngine;
using System.Collections;

public class NPC_Dialog : MonoBehaviour {

	//public BeginFight other; //this line will call a function from another script
	public string[] dialogue;
	bool displayDialog;
	

	// Use this for initialization
	void Start () {
		
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnGUI() {

		//this begins the place where text will appear
		GUILayout.BeginArea (new Rect (200,250,400,400));
		//if dialogue should be displayed and the quest has not been given, then 
		//display the dialogue
		if (displayDialog) {
			GUILayout.Label (dialogue[0]);
			

		}


	}

	void OnTriggerEnter(Collider other) {
		displayDialog = true;
		Debug.Log ("set to true");


	}

	void OnTriggerExit(Collider other) {
		displayDialog = false;

	}
}
