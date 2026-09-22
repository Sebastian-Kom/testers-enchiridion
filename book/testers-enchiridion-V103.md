# The Tester's Handbook

*A handbook for people who are paid to doubt*

A modern adaptation of Epictetus for software and systems testers.

Sebastian Komarnicki

Version 1.03  
22 September 2026

---

## 1. What Are We Responsible For?

Of Things, some are in our Power, and others not.

Verifying a claim, being willing to correct an error, and the honesty of your report are your responsibility. The machine’s behavior, the deadline requested by the customer, and other people’s reactions at the release meeting are not under your control.

If you make your peace of mind dependent on everyone welcoming a failed test, you’ve created a large committee that makes decisions for you.

So ask yourself: What does the evidence justify, and what is my role? Where you have decision-making authority, exercise it. Where you need someone else’s decision, make it clear what needs to be decided. Do not count a test that was not performed as one of your successes.

Practice assessing what the situation requires and acting wisely accordingly: that is **phronesis**. Through your repeated decisions, you shape your **ethos**—the character your colleagues come to rely on.

A green dashboard is encouraging. Make sure your representation of the situation reflects the truth.

## 2. Don’t Wish for the Result Before the Test

Remember that Desire promises the Attainment of that of which you are desirous; and Aversion promises the Avoiding of that to which you are averse: that he who fails of the Object of his Desire, is disappointed: and he who incurs the Object of his Aversion, wretched.

Before you run the test, notice which answer you desire. If you long for a pass, failing will seem like an inconvenience. If you long to prove the developer wrong, passing the test will seem like an injustice. You’ve found a way to be disappointed by a working machine.

Use only [the requisite Acts] of Pursuit and Avoidance; and even these lightly, and with Gentleness, and Reservation.

Investigate the suspected defect and let the evidence determine whether your suspicion is justified. If the product is fine and your test is wrong, adjust the test. You were hired to learn about the system. You don’t also have to win a prophecy contest.

## 3. Your Favorite Tool Is Transient

With regard to whatever Objects either delight the Mind, or contribute to Use, or are loved with fond Affection, remember to tell yourself, of what Nature they are, beginning from the most trifling Things.

If you value a framework, remember: It’s software. It has dependencies and maintainers. It hasn’t made any agreement to outlast your projects.

Make good use of it as long as it serves its purpose. Keep the significance of your tests understandable beyond just the syntax, and figure out what loss would prevent you from moving forward. You don’t need to buy a second lab just because a cable might break.

And if a colleague has knowledge you need, learn together.
Its continued availability is a hope, not a feature of the corporate culture. And learn to distinguish between availability and cooperation.

## 4. Before the Release Meeting

When you are going about any Action, remind yourself of what Nature the Action is.

When you go to a release meeting, imagine what will happen there: interruptions, hasty assurances, someone claiming that every defect is merely cosmetic. Tell yourself: “I will help us reach a decision while maintaining my sound judgment.”

If a colleague interrupts you, ask which evidence answers the disputed point. If their answer is sound, use it. You didn’t come to preserve your slides from corrections.

Also remember that you might be the one causing the commotion. Before you complain about the meeting being disorganized, check to see if you’ve brought a six-minute introduction to a question that only requires one sentence.

## 5. Before You Blame the Developer

If a test fails, don’t immediately declare that you’ve found a mistake made by the developer or the AI assistant. You, too, interpret requirements, write code, and craft prompts. Your title doesn’t grant any of these activities infallibility.

It is the Action of an uninstructed Person to lay the Fault of his own bad Condition upon others; of one entering upon Instruction, to lay the Fault on himself; and of one perfectly instructed, neither on others, nor on himself.

The tester who is making progress examines the requirement, the product, and the test, and lets the facts determine what needs to be corrected.

If the error is your fault, fix it and correct your report. You don’t need to attach a lengthy essay explaining why anyone could have made this mistake.

## 6. The Handsome Test Bench

Be not elated on any Excellence not your own.

If a test bench could say, “I can simulate a hundred faults,” we might forgive it for such boasting. But when you say, “I have a test bench like that, and I’m proud of it,” remember that you’re praising the test bench.

What, then, is your contribution? Deciding which error needs to be investigated, understanding what the result tells you, and acknowledging what remains unknown. If you’ve exercised this judgment well, take pride in your work.

Your AI model might suggest a test you could never have imagined. Welcome it, then verify what it demonstrates.

But don’t show me the number of channels when I ask you what you’ve learned.

## 7. Don’t Miss the Ship

Just as you can collect seashells on a sea voyage while the ship is at anchor, you can improve a useful script in your work. But keep in mind that you might be needed elsewhere.

Consider the consequences of a delay and the people who are waiting. Determine which duty deserves priority. Every incoming ticket will gladly appoint itself captain.

But if the Captain calls, run to the Ship, leave all these Things, regard none of them.

Once the more important task is clear, bring your improvements to a state where you can return to them later. And remember that the ship may also be waiting outside the office. Your family doesn’t need a ticket number before their claim on your time becomes real.

## 8. Reality Does Not Read the Specification

Require not Things to happen as you wish; but wish them to happen as they do happen; and you will go on well.

If the machine moves even though it’s supposed to stop, protect those it might harm and determine what happened. The machine wasn’t present at the meeting where its proper behavior was promised.

You can’t investigate a mistake while insisting that it has no right to exist.

## 9. A Blocked Test Is Not the End of the Evaluation

The controller is missing. What did it prevent? This measurement. Did it also prevent you from verifying the expected result, learning from yesterday’s log, or asking about the missing equipment?

For you will find it to be an Impediment to something else; but not to yourself.

Choose what moves the investigation forward. Don’t reorganize a hundred receipts just to give the appearance of a productive afternoon. If the missing controller is indispensable, make the dependency clear and look for an alternative plan.

And don’t report that the measurement was carried out. Resourcefulness has many uses. Manufacturing the past is not one of them.

## 10. What Virtue Does This Situation Call For?

Upon every Accident, remember to turn towards yourself, and enquire, what Powers you have for making a proper Use of it.

If the requirement is obscure, exercise curiosity. If the finding is unwelcome, courage. If the exploit invites you beyond the agreed assessment, restraint. When a colleague corrects you, try gratitude before eloquence.

Patience is useful while an investigation is unfolding. It becomes a flimsy excuse when someone is waiting for a response.

Ask yourself which quality serves the work here and to what extent. Even courage can become a nuisance if it insists on leading every meeting.

## 11. Responsibility Without Ownership

Never say of any thing, "I have lost it;" but, "I have restored it."

When a project passes to someone else, think of the traveler who must leave his lodgings. Take care of it as long as it is entrusted to you. Leave it in a condition suitable for the next person.

Hand over the supporting documents, the unresolved issues, and the knowledge necessary to understand them. Let your successor follow through on a task without having to rely on your memory. A folder titled “Final” is not a complete explanation.

If the handover is unfair, honestly object to it. Don’t make the work incomprehensible just to show how indispensable you were. You’ve succeeded if something useful can continue to exist without you.

## 12. What’s Worth Your Attention?

Begin therefore from little Things.

Is a ticket punctuated incorrectly? Correct it if it makes sense, and leave it at that. You don’t need to spend half an hour explaining where the comma belongs.

However, if a single incorrect bit changes the state of the machine, address the consequences. Small characters can trigger major commands. Ask yourself what the error results in before deciding how much attention it deserves.

You can give yourself some peace of mind by refraining from lecturing. But don’t buy that peace of mind by overlooking a danger.

## 13. Be Prepared to Not Know

If you would improve, be content to be thought foolish and stupid with regard to Externals.

If you don’t know what “normal operation” means in the requirement, ask. Maybe others know. Maybe everyone is hoping you do. Document the question, have the agreed-upon answer included in the requirement, and link your test to it. A conversation can clear your head while the specification remains obscure.

An AI assistant can help you formulate the question or find the answer. Don’t accept the answer just because it’s eloquent enough to make a follow-up question seem unnecessary or embarrassing.

Ask precise questions, verify what truly resolves the uncertainty, and learn. Once you understand it, apply what you’ve learned. You were not asked to permanently admit to being confused.

## 14. Don’t Make Approval Your Master

He is the Master of every other Person, who is able to confer, or remove, whatever that Person wishes either to have or to avoid.

If you can only report a failure once everyone is pleased to hear about it, consider who is now writing your report.

Strive for a fair hearing. Clarify an unclear explanation and correct an unfounded claim. But do not alter an observation just to elicit the smile that your evidence could not produce.

If speaking involves real costs, prepare yourself: preserve the evidence, seek advice, and choose your audience. You do not have to disregard your livelihood to speak honestly. Make sure that the desire for recognition does not determine the meaning of your assessments.

## 15. At the Banquet of Opportunities

Let projects, courses, and appointments appear before you like dishes at a banquet.

Put out your Hand, and take your Share, with Moderation.

Consider what you can make good use of, what you’ve already started, and who else is waiting. You have a workweek to digest your enthusiasm.

If a useful opportunity slips by, ask if another appointment can be scheduled. If you were overlooked, bring it up. Moderation doesn’t mean you have to go home hungry.

But don’t reach for every dish just because it’s within reach. Your plate may still bear witness to your appetite long after it has ceased to reflect your good judgment.

## 16. Show Compassion Without Panicking

If a colleague says, “I ruined the project,” give the person your full attention while you investigate the problem.

As far as Words go, however, do not disdain to condescend to him; and even, if it should so happen, to groan with him.

Listen. Help determine what happened, who might be affected, and what requires attention now. Neither repeat the judgment nor offer a cheerful acquittal before the facts are known.

Your colleague doesn’t have to calm down first to deserve your help. Bring enough composure to share the workload, and enough kindness to make it possible for them to share it with you.

## 17. Play the Role, Don’t Become the Costume

Remember that you are an Actor in a Drama, of such a Kind as the Author pleases to make it.

The job title on your door may remain the same, while the work behind it changes. Suppose a model now suggests tests that used to take up your afternoons. Figure out how this changes the contribution the team needs from you.

Review the new work together with your colleagues. Ask what you need to learn, what responsibilities you should take on, and what authority is required for this. A costume is a poor substitute for a rehearsal.

You can also question the script, negotiate your role, or look for a different stage. Whatever you do, figure out what it takes now to play the role well.

## 18. Even If the Raven Is Right

A raven croaks, and someone takes it as an omen of bad luck. At work, a colleague announces that the release is doomed. Suppose the bird and the colleague are both perfectly informed. The deadline will be missed, the product withdrawn, and your reputation bruised. Does any of this require you to conceal a finding, accuse someone unjustly, or invent a passing result?

For whichever of these things happens, it is in your power to derive advantage from it.

Use the warning to prepare, the fault to learn, and the difficulty to practice courage. Work to prevent the failure. If it comes nevertheless, help others face it honestly. The raven may know what awaits the project. It has not been appointed to govern you.

## 19. Decide What Counts as a Victory

You may be unconquerable, if you enter into no Combat, in which it is not in your own Power to conquer.

If your victory requires the developer to admit defeat, you’ve placed victory in someone else’s hands. Make it your mission to fairly examine the claim and contribute what the evidence warrants.

If a colleague refutes your finding, correct it. The system has not become any less understandable just because your name is missing from the list of heroes.

And if a valid objection remains unwelcome, continue on your path with the means at your disposal. Agreement is desirable. However, it is not a measure of whether the objection deserves to be raised.

## 20. Pause Before You Respond

A colleague calls your insight foolish. Your response is already excellent, especially the paragraph about the colleague.

For, if you once gain Time and Respite, you will more easily command yourself.

Set this paragraph aside for now. Outline the disputed claim, the evidence supporting it, and the question that would lead to clarification. If the personal remark requires a response, answer clearly and directly: Disagreement does not require insults.

You may find that three sentences accomplish what your anger had intended to cover in three pages.

## 21. Think About What Can Be Lost

A report states that an output remained active after a fault. Follow the signal: Could the machine have continued running, and who might have been in its path?

Let Death and Exile, and all other Things which appear terrible, be daily before your Eyes; but chiefly Death: and you will never entertain any abject Thought, nor too eagerly covet any thing.

When people rely on a stop function, examine the conditions under which it must protect them. Let the potential harm determine what you investigate and whom you involve in the decision.

Do not let a harmless-sounding description determine the severity of the finding. The operator will continue to encounter the machine long after the meeting is over.

## 22. Expect Ridicule, Not Applause

If you’re called the team’s philosopher because you ask what a claim is based on, don’t immediately slip into the role of the sage.

Now, for your Part, do not have a supercilious Look indeed; but keep steadily to those Things which appear best to you, as one appointed by God to this Station.

Consider whether the laughter contains useful criticism. Perhaps your question is necessary. Perhaps you asked for a treatise where a simple measurement would have sufficed. Correct the excess and retain the legitimate concern.

Don’t rehearse the speech you’ll give when everyone finally admires you. There’s still a test ahead.

## 23. Be a Tester

You say, “I am a tester.” Very well: What have you tested today?

Be contented then, in every thing, with being a tester: and, if you wish to be thought so likewise by any one, appear so to yourself, and it will suffice you.

Your **ethos** takes shape when you correct a flattering report, admit to an incorrect result, or investigate a doubt that won’t earn you any applause. Apply the same care when no one is watching, and share what others need to know.

Your profile may proclaim your virtues in the blink of an eye. Let your colleagues recognize them in your work.

## 24. Be Helpful Without Compromising Your Credibility

A colleague asks you to present the results in a more positive light so that a contract can be won. Ask what new evidence has been provided with the request.

Besides: which would you rather have a Sum of Money; or a Friend of Fidelity and Honour?

Offer help that stands up to scrutiny: qualify the claim, gather the missing evidence, or explain what still needs to be clarified. If a decision about a risk must be made, present the evidence and the uncertainties to those in charge.

Stay true to your colleague by ensuring your presentation is reliable. Friendship can’t force a test to pass.

## 25. The Price of a Seat at the Table

Before you envy someone else’s seat at the meeting, ask what it cost them. Perhaps it required a lot of preparation, patient explanations, and an understanding of what others must decide. If you refused to do that work, think of two people at a market: one buys the lettuce, and the other keeps the money.

For as he hath the Lettuces, so you have the Half-penny, which you did not give.

You can choose to pay a fair price. Ask for a hearing, prepare yourself, and make a useful contribution. If you’ve been wrongfully excluded, challenge that exclusion.

But if admission requires concealing a fact, consider what you would be giving up in return. A seat can be too costly, even if no money changes hands.

## 26. Your Mistake, My Mistake

Your colleague breaks a cup: “These things happen.” You break your own, and the laws of nature demand an investigation.

Be assured then, that, when your own Cup likewise is broken, you ought to be affected just as when another's Cup was broken.

If the error lies in a supplier’s controller, you call it serious. If it lies in your own, you note how unusual the circumstances are.

Swap the names while retaining the relevant facts. Would the evidence, the consequences, or the necessary correction change? If the circumstances differ, examine the difference. If only the party responsible differs, leave the severity assessment unchanged.

## 27. Missing the Mark

As a Mark is not set up for the Sake of missing the Aim, so neither doth the Nature of Evil exist in the World.

The developer intended for the controller to respond correctly but assumed that every sensor value would be valid. The code adhered more closely to this assumption than to reality.

Look for where the intended function fell short: in the requirement, in the design, in the code, or in their interaction with actual conditions. Suggest a correction for the error and verify that the correction serves the intended purpose.

You may find an incorrect assessment without finding anyone who intended its consequence.

## 28. Do Not Surrender Your Judgment

Someone calls your insight absurd, and for the next hour you can think of nothing but that insult.

And do you feel no Shame in delivering up your own Mind to be disconcerted, and confounded by any one, who happens to give you ill Language?

Return to the assertion. What supports it? What would prove it wrong?

Treat flattering feedback or a confident AI explanation with equal care. Let both improve your judgment by providing you with reasons you can examine. If these reasons refute your conclusion, change it.

Do not let the loudest voice decide the expected result.

## 29. Before You Compete in the Test Olympics

In every Affair consider what precedes and follows; and then undertake it.

You want to win at the Olympics. You imagine the crown. Now imagine the training, the coach’s corrections, and the possibility of defeat.

Do the same before you commit to an AI testing service. Who will get up to speed on the unfamiliar work, review the tests, maintain the environments, and analyze the errors? What scope has been approved, and what will support the service after the demonstration?

Start with a project that you can prepare, maintain, and evaluate. Expand it if there’s a reason to do so.

You can order the victory wreath today. It won’t give you any additional skills.

## 30. Duty Is Not Blind Obedience

Duties are universally measured by Relations.

You are a colleague and a team member. You also help make decisions that an operator can rely on. Think about all these relationships when someone says, “Be loyal.”

If you’re instructed to mark an unperformed safety test as passed, refuse to make the false entry. Indicate what remains unknown, document your concerns, and seek a responsible decision through the appropriate channels. Help set a course based on the truth.

If a properly authorized decision permits work to continue with a disclosed limitation, document that decision as such. This does not make up for the missing test.

Loyalty should make your account trustworthy.

## 31. Go with the Flow

If the system resists your plan, consider what is more important to you: the purpose of the work or the honor of having planned it.

For where Interest is, there too is Piety placed.

Don’t become so absorbed in your diagram that you stop looking at the machine.

A swimmer gets to know the current. Study the conditions, choose a limited experiment whose potential consequences you can responsibly contain, and observe what changes. Decide in advance when you’ll stop. If you can’t contain the consequences, find another way to learn.

Let what happens guide the next step. It is unlikely that the river will improve its behavior if it receives yet another copy of your approach.

## 32. The Oracle Can Advise, but It Cannot Excuse You

An oracle predicts a peaceful outcome. Before you feel reassured, ask what the prediction is based on and what remains untested. A favorable prediction does not make up for the missing test. Point out the gap, even if the oracle expects that no one will suffer as a result.

When, therefore, it is our Duty to share the Danger of a Friend, or of our Country, we ought not to consult the Oracle, whether we shall share it with them, or not.

Consult your AI model about the consequences, competing duties, and people you may have overlooked. Let it question a convenient excuse just as readily as a technical assumption. Examine its reasoning and the available evidence. Present unresolved questions to the decision-makers.

You can consult the oracle. Nevertheless, you must take responsibility for what you do with its advice.

## 33. Conduct in the Lab and in Society

Choose a character that you can maintain both at the lab bench and in meetings. Your **ethos** should not require a change of clothes when management arrives.

**Speak thoughtfully.** Be for the most part silent: or speak merely what is necessary, and in few Words. State what you have found, what supports it, and what remains uncertain. Necessary words also include an unwelcome warning.

**Listen attentively.** Understand your colleagues’ arguments well enough to paraphrase them fairly. While they are speaking, do not devote your full attention to planning an interruption.

**Act with discretion.** Protect confidential information from prying eyes. Pass on important findings to those who need to act on them. Assess what each person needs to know.

**Disagree respectfully.** Challenge the claim firmly and provide a rationale. A flaw in an argument does not justify humiliating the person who made it.

**Practice humility.** Admit your mistake, correct it, and acknowledge those who helped you. A critic who mentions only one of your mistakes may simply be short on time.

**Prepare for authority.** Organize the evidence, explain the consequences, and make it clear what decision is required. Prepare for a negative reaction without letting it dictate your own conduct.

Practice these habits even when no one is applauding. Your colleagues should be able to rely on more than just your performance in front of an audience.

## 34. Before Taking the Easy Shortcut

The pipeline would be green if only this pesky test were eliminated. The fix seems to require very little understanding of the error.

If you are struck by the Appearance of any promised Pleasure, guard yourself against being hurried away by it: but let the Affair wait your Leisure, and procure yourself some Delay.

Think of the relief you’d feel now and the decision someone will make tomorrow based on that green result. Determine what the test is checking and why it’s failing.

If it’s justified to set it aside, document what remains unresolved, the compensating checks, the person responsible, and the date for re-evaluation. Make the exception visible.

A temporary workaround shouldn’t become the team’s longest-standing member.

## 35. Stand Behind a Justified Action

You have reason for serious concern, but you may not like the reaction you expect.

When you do any thing from a clear Judgment that it ought to be done, never shun the being seen to do it, even though the World should make a wrong Supposition about it: for, if you do not act right, shun the Action itself; but, if you do, why are you afraid of those who censure you wrongly?

Examine these reasons once more. If they hold up, present the findings, their limitations, and the course of action you recommend to those who need to address them. Keep the evidence and accept a justified correction.

You need a responsible audience. The entire Internet doesn’t have to listen.

## 36. Don’t Take Up the Whole Bench

You’ve been occupying the shared bench all week and boasting about your impressive productivity. At the banquet, you ate the largest helping and praised the efficiency of your appetite.

When you eat with another, then remember, not only the Value of those Things which are set before you, to the Body; but the Value of that Behaviour, which ought to be observed towards the Person who gives the Entertainment.

Ask whose work is waiting while yours is in progress. Compare the decisions each use of the bench would support, the consequences of a delay, and the work that cannot wait.

Agree on an allocation of bench time that serves the overall project. Leave room for urgent matters where a delay would be significant, and explain the priorities to those sitting at the table with you.

## 37. Promise Only What Is Within Your Competence

If you have assumed any Character above your Strength, you have both made an ill Figure in that, and quitted one which you might have supported.

Your new title arrived before the knowledge it seems to promise. Emphasizing it even more boldly will not close that gap.

Ask yourself what the assessment requires, what you can responsibly do now, and where qualified support is needed. Secure that support, limit your commitment, or decline the part for which there is no support. Identify the work you would have to give up if you accept.

Perhaps you will learn to play a greater role. Give yourself time to learn before you promise a performance that others must rely on.

## 38. Protect Your Judgment

As, in walking, you take care not to tread upon a Nail, or turn your Foot; so likewise take care not to hurt the ruling Faculty of your Mind.

Before tackling a difficult assessment, take enough time to follow the line of reasoning. Ask yourself what would contradict your preferred explanation, and look for it.

When another person or a model reviews your work, have them reexamine the evidence and premises. Two answers derived from an unchecked assumption are not two independent reasons.

You schedule maintenance windows for the server. Give its auditor some protected time as well.

## 39. An Appropriate Testing Strategy

The Body is to every one the measure of the Possessions proper for it; as the Foot is of the Shoe.

A shoe that fits is useful.
Gilding it does not make the foot any bigger. Adding gemstones can make walking difficult.

Identify the claims your examination must support, the conditions that matter, and the requirements that must be met. Determine what evidence would be sufficient, what further work might change the decision, and what uncertainty remains.

Explain why you are stopping, including what remains untested. If further evidence is required, obtain it. If an ornament adds nothing to the investigation, leave it with the jeweler.

Nor should you consider a shoe that’s too tight to be appropriate just because it was cheap.

## 40. Don’t Settle for Something That Merely Looks Like It Has Been Tested

If a positive report is met with applause, you might start designing tests primarily to ensure it remains positive.

You’re showing that a command was accepted. Does your test also show that the required action follows under the relevant conditions and within the critical timeframe? If the claim were false, what in your test would reveal this?

Choose a relevant challenge. Make sure the expected result and the observations can distinguish between success and failure. If the product passes the test, celebrate the success. If the test is flawed, correct it.

A test that cannot detect the relevant error is easy to pass.

## 41. Support the One Who Judges

You must eat, exercise, and take care of your body.

These should be done incidentally, and slightly; and our whole Attention be engaged in the Care of the Understanding.

But caring for the mind must not mean neglecting the one who understands. Allow yourself appropriate breaks and give a difficult finding time to be examined.

If meetings and routine updates take up this time, question the organization. If you can no longer thoroughly review the matter, take a break or find another reviewer while you attend to everything that cannot wait.

A fully charged laptop does not mean its owner is fully prepared.

## 42. Understand Their Perspective, Don’t Invent Motives for Them

A developer rejects your findings. Before you write a report about their arrogance, remember:

It seemed so to him.

Ask what makes the result acceptable from their perspective. Perhaps they expect a different configuration. Perhaps they have evidence you haven’t seen. Perhaps their assumption is wrong. Find out.

Describe what you observed, and examine the disagreement together. If their reasoning is sound, correct your account. If it isn’t sound, keep an eye on the issue and take the necessary steps.

You need to make a statement. You don’t need to invent your opponent’s backstory as well.

## 43. Choose the Handle That Lets You Carry It

Every Thing hath two Handles; the one, by which it may be borne; the other, by which it cannot.

One handle says, “You’re blocking my approval.” The other says, “We need to decide what this unresolved issue means for the machine’s users.”

Take the second one and make it concrete: What evidence is missing, what consequences matter, and who needs to take action?

Keep the bug in sight while you change the way you approach it. You haven’t made the burden any lighter by hiding part of it.

Agree on the next investigation and the person responsible for it. This is a useful step toward moving the matter forward.

## 44. More Tests Do Not Mean Better Testing

These Reasonings are unconnected: "I am richer than you; therefore I am better:" "I am more eloquent than you; therefore I am better."

“We have ten times as many tests,” you say. So we have ten times as many tests. What else follows from that?

Examine what different behaviors they cover, what errors they might uncover, and what relevant conditions remain untested. A model can multiply good tests or reproduce a single gap with remarkable zeal.

Count what helps you in your assessment, and explain what the count means. State the claim supported by your evidence.

A larger whole number has not yet won an argument simply by appearing.

## 45. Describe Before You Judge

A colleague finishes a review quickly. You claim that he was careless. First, think of the man taking his shower in a hurry.

Do not say, that he doth it ill; but, in a mighty little time.

In the report, write down what you observed, where the record came from, and what conclusions you draw. A screenshot may show an output. However, it does not necessarily show the configuration that generated it. A conversation recounted from memory should be labeled as a recollection.

Look for the crucial context. Take necessary precautions as long as uncertainty remains.

Hold off on the adjective until the evidence is available.

## 46. Be Useful, Even When Overlooked

Do not make recognition the price of your help.

For remember, that in this manner Socrates also universally avoided all Ostentation.

People asked Socrates to recommend a philosopher, overlooking that he was one himself. He helped them find one. He did not begin by explaining whom they had failed to recognize.

If a colleague asks you where to find a good tester, consider what they need. Offer your help if you can; introduce someone better suited if you cannot. Let what you have learned appear in a well-chosen question, a careful investigation, or a patient explanation.

If the problem is solved and someone else receives the thanks, the problem is still solved.

## 47. Practice Without Performing Feats

When you have brought yourself to supply the Necessities of your Body, at a small Price, do not pique yourself upon it: nor, if you drink Water, be saying upon every Occasion, "I drink Water."

You’re proposing an all-night rehearsal to prove your commitment. Ask yourself what skill this fosters and why exhaustion is necessary.

Practice in an authorized environment designed to contain the exercise’s effects.
Set a goal and an endpoint. Practice assessment, communication, and handoff. Afterward, examine what was overlooked and share the insights and recognition.

If the same emergency recurs every week, question the situation that requires your heroic action.

The exercise should better prepare you for the job.

## 48. Evaluate the Reviewer

A tester can improve and must still maintain that improvement.

But he goes about with the Caution of infirm People [after Sickness, or an Accident], dreading to move any thing that is set right, before it is perfectly fixed.

Review one of your own decisions. What did you know at the time? What alternatives did you consider? Which assumption carried the most weight? Ask a colleague to challenge that assumption before you present your preferred defense.

Then examine the result. A lucky coincidence does not make up for poor reasoning. An undesirable result does not in itself condemn sound reasoning.

Maintain the habit you are still learning.

## 49. From Interpreting the Standard to Testing the System

You can explain the standard wonderfully. An interpreter could just as easily explain the Stoic philosopher Chrysippus. What follows from the explanation?

And when I find an Interpreter, what remains is, to make use of his Instructions.

Take a requirement. Determine which version and configuration it applies to, obtain an agreed-upon, documented clarification if necessary, and state what behavior would satisfy it. Select the conditions, observations, and expected result that will allow you to verify this claim.

Trace the result through to the decision it supports. A link in a traceability table deserves just as much scrutiny as the statements it connects.

The machine has no objection to an elegant explanation. However, it may fail in the process.

## 50. The Practice Begins with This Decision

“I’ll improve the practice after the next tool rollout,” you say. This resolution has already survived several tools.

And if any Instance of Pain, or Pleasure, or Glory, or Disgrace be set before you, remember, that now is the Combat, now the Olympiad comes on, nor can it be put off; and that, by once being worsted, and giving way, Proficiency is lost, or [by the contrary] preserved.

Choose whatever today’s work allows: correct the dubious claim, ask the necessary question, or provide a colleague with the evidence they need. Do this with the care that the situation demands.

Stay true to your commitment to honest research. Revise a method when the evidence calls for it, and start over if you fail.

The next quarter will bring plenty of work.

## 51. Phronesis Is More Than Just Explaining the Rule

First: Report honestly.

Second: Understand why you owe honesty to those who must rely on the report.

Third: Examine the arguments you use to justify this obligation. These latter considerations should help you fulfill the first.

Therefore, at the same time that we lie, we are mighty ready to show how it is demonstrated, that Lying is not right.

Your explanation is excellent. However, the unfinished task is still marked as completed in the file. Correct the entry, inform those who rely on it, and make or obtain a responsible decision regarding the missing work.

Here lies an opportunity for **phronesis**: Understand what matters in this specific decision, and act accordingly.

## 52. Keep These Questions Handy

Upon all Occasions, we ought to have these Maxims ready at hand:

Let the evidence set the limits of the claim. **What is known?**

Keep in mind the people who will bear the consequences. **Who is affected?**

Be mindful of the responsibility that falls on you. **What is my task?**

Keep your judgment open to correction. **What would make me change my mind?**

Keep them ready. The next opportunity won’t announce itself as philosophy.

---

*Source: Epictetus, The Enchiridion, translated by Elizabeth Carter, in [All the Works of Epictetus, Which Are Now Extant (Dublin, 1759)](https://archive.org/details/allworksofepicte00epic), pp. 387–412; §29 follows Discourses III.15, p. 236, as directed by that edition. Deliberate adaptations are documented in the separate V103 source record.*

© 2026 Sebastian Komarnicki. The original modern adaptation is licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/). Carter’s historical text remains public domain. When sharing an adaptation, credit the author, link to the edition used and the license, and indicate your changes.
