# prompt_design_rationale.md

## Prompt Design Rationale

This document explains the reasoning, design decisions, and lessons learned during the development and evaluation of the prompt templates used in the Generative AI component of the employee attrition explanation system.

The objective of the prompt engineering process was to explore how different prompt structures affect the quality, readability, personalization, and usefulness of AI-generated explanations related to employee attrition predictions.

---

# 1. Template 1 – Basic Explanation (T1)

## Thought Process Behind the Template

The first template was intentionally designed to be simple and general. The goal was to create a baseline prompt capable of generating easy-to-understand explanations without adding excessive structure or constraints.

This template focused mainly on:

* simplicity
* accessibility
* basic interpretation of predictions

The design intentionally avoided highly detailed instructions to observe how the model behaves with minimal guidance.

---

## Influence of Domain Knowledge

Knowledge of employee attrition factors influenced the inclusion of employee attributes such as:

* job satisfaction
* overtime
* work-life balance
* years at company

However, the template did not explicitly instruct the model to deeply analyze these factors, resulting in broader explanations.

---

## Observations During Testing

During testing, T1 consistently generated:

* clear and readable explanations
* simple summaries suitable for non-technical users

However, the outputs were often:

* generic
* less personalized
* lacking actionable recommendations

This demonstrated that simple prompts improve readability but reduce analytical depth.

---

# 2. Template 2 – Structured HR Analysis (T2)

## Thought Process Behind the Template

T2 was designed to improve organization and consistency by introducing structured analytical sections.

The template explicitly instructed the model to provide:

1. Main factors behind the prediction
2. Risk level
3. Recommended HR actions

The goal was to encourage more systematic reasoning and reduce randomness in generated outputs.

---

## Influence of Domain Knowledge

HR domain knowledge strongly influenced the structure of this template. HR professionals commonly evaluate:

* attrition risk factors
* employee engagement
* retention strategies

Therefore, the prompt was designed to imitate a structured HR assessment process.

---

## Observations During Testing

T2 generated:

* more organized outputs
* stronger analytical reasoning
* improved alignment with HR-related concepts

However, some outputs became:

* repetitive
* overly formal
* less conversational

The testing showed that structured prompts improve consistency and reasoning quality but may reduce natural conversational flow.

---

# 3. Template 3 – Manager-Friendly Explanation (T3)

## Thought Process Behind the Template

T3 was designed specifically for managers and non-technical decision-makers who need quick and understandable summaries rather than detailed HR analysis.

The template emphasized:

* conversational communication
* concise explanations
* direct recommendations

The phrase “Let me break it down in simple terms” was intentionally used to encourage more natural and accessible language generation.

---

## Influence of Domain Knowledge

Managers often prioritize:

* quick understanding
* actionable summaries
* operational decision-making

Therefore, the template focused less on deep analysis and more on practical communication.

---

## Observations During Testing

T3 consistently produced:

* highly readable outputs
* conversational explanations
* manager-oriented recommendations

Interestingly, despite being designed as a concise template, the generated responses were often longer than expected because the model expanded explanations and recommendations naturally.

The testing demonstrated that conversational prompts significantly improve readability and accessibility.

---

# 4. Template 4 – Personalized Retention Advice (T4)

## Thought Process Behind the Template

T4 was designed to maximize:

* personalization
* relevance
* practical usefulness

Unlike the other templates, T4 explicitly instructed the model to:

* identify employee-specific risk factors
* explain their relationship to attrition
* generate personalized retention recommendations
* avoid unsupported assumptions

The objective was to create outputs suitable for realistic HR support scenarios.

---

## Influence of Domain Knowledge

Employee attrition is influenced by multiple contextual factors, including:

* job satisfaction
* overtime
* compensation
* work-life balance
* tenure

HR retention strategies also rely heavily on personalized interventions rather than generic explanations. This influenced the decision to require individualized recommendations within the prompt structure.

---

## Observations During Testing

T4 consistently produced:

* the most detailed outputs
* highly personalized explanations
* actionable HR recommendations

The outputs demonstrated strong alignment with employee retention concepts and practical HR workflows.

However, the increased detail also:

* reduced readability
* increased response complexity
* produced denser analytical text

Despite these limitations, T4 achieved the strongest overall performance and was selected as the best template for integration into the final system.

---

# Lessons Learned During Prompt Testing

Several important lessons were learned during the prompt engineering process:

1. Prompt structure significantly affects output quality
   Simple prompts improve readability, while structured prompts improve reasoning and consistency.

2. More detailed prompts improve personalization
   Templates with explicit instructions about employee context generated more relevant and actionable explanations.

3. Conversational prompts improve accessibility
   Templates using natural language and conversational framing produced easier-to-read outputs.

4. Increased detail reduces readability
   Templates generating highly analytical outputs often produced lower readability scores due to longer and denser explanations.

5. Generative AI outputs remain variable
   Even with fixed prompts, generated outputs may vary between runs due to the probabilistic nature of large language models.

---

# Prompt Engineering Best Practices Applied

The prompt templates were designed using several prompt engineering best practices, including:

* Clear role assignment (e.g., HR assistant, HR analyst, manager)
* Explicit task instructions
* Structured output formatting
* Context injection using employee features and prediction results
* Constraint-based prompting to reduce hallucination
* Audience-aware communication style
* Instruction refinement through iterative testing

