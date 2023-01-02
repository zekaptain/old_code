using UnityEngine;
using System.Collections;

[RequireComponent(typeof(CharacterController))]

public class MyEnemyAI : MonoBehaviour {

	enum CharacterState {
		Idle = 0,
		Walking = 1,
		Trotting = 2,
		Running = 3,
		Jumping = 4,
		Attacking = 5,
	}
	
	private CharacterState _characterState;

	public float fpsTargetDistance;
	public float enemyLookDistance;
	public float attackDistance;
	public float enemyMovementSpeed;
	public float damping;
	public float moveSpeed;
	float t;
	//somehow set this tranform to equal Warrior_example1
	public Transform fpsTarget;
	Rigidbody theRigidbody;


	//this variable stores the Animator on our character model
	internal Animator animController;

	void Awake() {

		//should i find the character's anim controller here? idk
		//find the character model's Animator component and store it
		animController = GetComponentInChildren<Animator>();

	}

	// Use this for initialization
	void Start () {
		//should this be rigidbody or animator controller?
		theRigidbody = GetComponent<Rigidbody> ();
		fpsTarget = GameObject.Find ("Warrior_example1").transform;
		//= GameObject.FindGameObjectWithTag("Player").transform

	}
	
	// Update is called once per frame
	//this is fixed update because we're using a rigidbody
	void FixedUpdate () {
		//should only attack if the scene is arena env, where the fight takes place
		//looked at build settings -- arena env is 2 on build settings, and Application.loadedLevel is an int
		//this works, yay!
		if (Application.loadedLevel == 2) {
			fpsTargetDistance = Vector3.Distance (fpsTarget.position, transform.position);
			if (fpsTargetDistance < 20f){//enemyLookDistance) {

				lookAtPlayer ();
				//print ("Look at player please");
			}
			if (fpsTargetDistance < 12f && fpsTargetDistance >= 3f ) {

				chase ();
				print ("chasing player");
			}
			if (fpsTargetDistance < attackDistance) {

				attackPlease ();
				print ("Attack!");
			} else {
				//stays idle
				_characterState = CharacterState.Idle;

			}
		} else {
			//basically stay idle
			_characterState = CharacterState.Idle;

		}

		//this line sets the CharacterState parameter on the character model's animator controller every frame
		animController.SetInteger("CharacterState", (int)_characterState);
	}

	void lookAtPlayer() {
		//t = Time.deltaTime;
		//Quaternion rotation = Quaternion.LookRotation (fpsTarget.position - transform.position);
		//transform.rotation = Quaternion.Slerp (transform.rotation, rotation, Time.deltaTime * damping);
		//quaternion wouldn't work -- this is more sharp but it does the job
		transform.LookAt (fpsTarget.transform);
		print ("Look at player please");
		_characterState = CharacterState.Idle;
	}
	//make this faster for better players
	void chase() {
		transform.Translate (Vector3.forward * moveSpeed * Time.deltaTime);
		_characterState = CharacterState.Running;
	}

	void attackPlease() {
		//this is for a rigid body -- need to modify for character controller
		//did this -- chase function above moves character towards player
		theRigidbody.AddForce (transform.forward*enemyMovementSpeed);
		_characterState = CharacterState.Attacking;
	}
}
