using UnityEngine;
using System.Collections;

public class ChangeScenes : MonoBehaviour {
	
	// Use this for initialization
	void Start() {
		
	}
	void Update() {
		
	}
	void OnGUI(){
		if (GUI.Button (new Rect(320,180,90,50), "Start Game")) {
			Application.LoadLevel ("mainEnvironment");
		}
	}
	
}