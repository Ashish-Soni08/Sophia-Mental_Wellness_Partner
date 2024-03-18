# StartUp Idea

## Setup the Virtual Environment

<!-- ```bash

# python version -> 3.10.13(Github Codespaces) -> 3.10.10(Lightning Studios)
python -V 

# create a environment named -> geek_env
python -m venv geek_env

# activate the environment
source geek_env/bin/activate

``` -->

## Chatbot for Mental Well-being

### Problem Statement

[In **2017**, findings from the National Mental Health Survey revealed that approximately **one** out of every **seven** individuals in **India** experienced mental health issues such as depression and anxiety. This heightened awareness of mental well-being has elevated its significance as a focal point for development initiatives. Nearly **150** million individuals in **India** were identified as requiring interventions, with a disproportionate burden observed among the lower and middle-income populations compared to their wealthier counterparts](https://github.com/pandeyanuradha/Chatbot-for-mental-health?tab=readme-ov-file#motivation-behind-this-project)

Mental health is a complex issue and addressing mental health demands the highest level of attention and care. Unlike many other health concerns, mental health issues often intertwine with various aspects of an individual's life, including their social environment, personal experiences, and genetic predispositions. Additionally, the stigma surrounding mental health further complicates the matter, hindering individuals from seeking help and society from providing adequate support systems.

### Objective

The main **goal** of this project is to `provide a support system for an individuals's mental well-being.`

Generative AI has ushered in a new era for chatbots, providing them with capabilities to engage users in more natural conversations. Generative AI models also known as LLMs(Large Language Models) have given us the opportunity to offer more personalized and foster more engaging interactions. But deplying these LLMs in consumer applications poses several challenges, including the need to add guardrails that prevent the model from generating undesirable responses. For example, in the context of building an AI for mental health, then you don't want it to generate toxic answers that bring more mental distress or teach people to engage in behaviors harmful to oneself.

To align these LLMs according to a set of values, researchers at Anthropic have proposed a technique called [Constitutional AI](https://www.anthropic.com/news/constitutional-ai-harmlessness-from-ai-feedback) (CAI), which asks the models to critique their outputs and self-improve according to a set of user-defined principles.

Afer aliging the model, it is important to have the right prompt to guide the model to generate meaningful responses that promote mental well-being, the idea is to explore `Role based prompt engineering` technique, so that the model can generate responses that are consistent with principles from **Adlerian Psychology** [Inspiration](https://www.goodreads.com/en/book/show/43306206) . Please refer to the table below for some of the principles and their advantages.

| Principle                           | Advantage                                                                                                            |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Encouragement and Empowerment**  | Fosters **self-efficacy** and **resilience**, providing supportive guidance to build user confidence in coping with challenges. |
| **Goal Orientation**               | Promotes setting meaningful **goals** and developing actionable strategies, fostering a sense of **purpose** and **direction**.   |
| **Social Interest**                | Emphasizes the significance of **social connection** and **community involvement**, enhancing a sense of **belonging**.          |

Utilizing role-based prompt engineering alongside these principles ensures that the model generates responses that are consistent with Adlerian Psychology, thereby enhancing the effectiveness and relevance of the chatbot's interactions.

## Implementation Strategy

### Generating a CAI dataset

Create Synthetic Data with LLMs using `llm-swarm`. Build two datasets, an SFT dataset and a preference dataset.

### Models

***CHAT MODEL*** - The idea is to use Constituional AI to bake in harmlessness into the `Llama-2-7b-chat-hf` model and following that, employ prompt engineering techniques to integrate `Adlerian psychology principles` into the model.

***MODERATION MODEL*** - `LlamaGuard-7b` a safeguard model to ensure user inputs and model responses are safe.

## References

- [Project Motivation](https://github.com/pandeyanuradha/Chatbot-for-mental-health?tab=readme-ov-file#motivation-behind-this-project)
- [HuggingFace Blog Post on Constitutional AI](https://huggingface.co/blog/constitutional_ai)
- [Adlerian Psychology Book Summary](https://www.kadlac.com/notes/the-courage-to-be-disliked)

## License

The content of this repository is licensed under a [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
