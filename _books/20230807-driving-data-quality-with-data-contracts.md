---
authors:
- andrewjones
cover: images/books/20230807-driving-data-quality-with-data-contracts/cover.jpg
description: Book of the Week. Driving Data Quality with Data Contracts by Andrew
  Jones
end: 2023-08-11 23:59:59
image: images/books/20230807-driving-data-quality-with-data-contracts/preview.jpg
links:
- link: https://data-contracts.com/
  text: Book's website
- link: https://www.packtpub.com/product/driving-data-quality-with-data-contracts/9781837635009
  text: Book's page
- link: https://www.amazon.com/Driving-Data-Quality-Contracts-comprehensive-ebook/dp/B0C37FPH3D/?&_encoding=UTF8&tag=arj0a-20&linkCode=ur2&linkId=f92a47437dd6991cc35db95963846030&camp=1789&creative=9325
  text: Buy on Amazon
start: 2023-08-07 00:00:00
title: Driving Data Quality with Data Contracts

archive:
- name: Joe Edgerton
  text: What would you say is the low-hanging fruit that companies/orgs could do to
    more easily adopt data contracts? I'm interested in learning more about data governance
    because we don't have any data experts on my small team and we constantly run
    into issues that you've described. It sounds like chpt. 3 addresses this, and
    part 2 overall seems to get at the "why/what" for contracts. Thank you!
  replies:
  - name: Andrew Jones
    text: "Hey Joe Edgerton, great question!\nI\u2019d say the low handing fruit and\
      \ first step is to get people talking to each other! When there is an upstream\
      \ change that breaks a data process, set up a meeting to discuss it. Make the\
      \ engineering team aware of the issues the data team are facing, and the impact\
      \ it has (or could have, for example if you have data process that are critical\
      \ to the business).\nThose conversations will naturally start leading to discussions\
      \ around how to prevent these issues. That\u2019s when you can start to introduce\
      \ data contracts as an idea to consider.\nThat\u2019s really all it takes! People\
      \ want to do the right thing for the organisation, but too often data teams\
      \ suffer in silence, so other parts of the business are just not aware. Data\
      \ teams also attempt to work around these issues, but that just increases complexity\
      \ and makes the pipelines even more reliable, as well as more expensive.\nA\
      \ similar approach can be taken to any data governance initiative. Get the right\
      \ people together, clearly articulate the problems you\u2019re having _and_\
      \ the impact or cost it has on the business, and get everyone bought in to finding\
      \ a solution. That gives everyone a sense of ownership of the problem and incentivises\
      \ them to help out on a solution."
  - name: Joe Edgerton
    text: Thanks!
- name: Hrithik Kumar
  text: Could you elaborate on how establishing data contracts as interfaces can help
    assign responsibility and accountability for data to its generators? How does
    this autonomy benefit the data management process?
  replies:
  - name: Andrew Jones
    text: "Hey Hrithik Kumar,\nGreat question, as this is a lot of what data contracts\
      \ is all about!\nThere\u2019s a few ways data contracts as interfaces help assign\
      \ responsibility and accountability for data to its generators.\nSimply the\
      \ act of calling this an interface helps a lot, as software engineers work with\
      \ interfaces all the time. It automatically implies something that they are\
      \ providing for a consumer, and that they are committing to maintaining. What\
      \ we\u2019re saying with data contracts is that it\u2019s no different to an\
      \ API, a library interface, etc, and you have the same responsibilities for.\n\
      But, if you\u2019re responsible for something, you need to have the autonomy\
      \ to fully manage it, otherwise you wont feel like an owner. I\u2019m sure many\
      \ of us here has worked in a team where a service was given to us and we were\
      \ expected to own it, despite having no say it how it was developed and no confidence\
      \ in making changes to it. It\u2019s not a nice feeling! We don\u2019t feel\
      \ like an owner, and we\u2019re not motivated to support it.\nThat\u2019s why\
      \ data generators have to own the contract. They need to be comfortable with\
      \ the data they are providing, its structure, its SLOs. They need to have the\
      \ ability to change those things as requirements or technical limitations change\
      \ over time.\nTo support this autonomy we need to provide them with tooling\
      \ that enables them to create and modify data contracts without review/gatekeeping/approval\
      \ from a central team slowing them down. Ideally, that tooling will be as good\
      \ as the tooling they use to build an API, or spin up a database on a cloud,\
      \ etc. Most of us aren\u2019t there yet, but in a few years this will be the\
      \ norm.\nHope this helps! I go it to this in a lot of detail in the book, and\
      \ the word _autonomy_ might be the most common word of the book! But do let\
      \ me know if you have any follow up questions and I\u2019ll be happy to answer\
      \ \U0001F642"
  - name: Hrithik Kumar
    text: 'Thank you for the detailed response. I have a follow up question on that.

      Could you share insights on how organizations can transition towards embracing
      data contracts and the potential challenges associated with this transformation?'
  - name: Andrew Jones
    text: "Sure!\nThe answer I gave to the question above on low hanging fruit has\
      \ good advice on how to get started: [https://datatalks-club.slack.com/archives/C01H403LKG8/p1691593111422599?thread_ts=1691581909.592479&amp;cid=C01H403LKG8](https://datatalks-club.slack.com/archives/C01H403LKG8/p1691593111422599?thread_ts=1691581909.592479&amp;cid=C01H403LKG8)\n\
      Basically, identify where they add most value and start there. Build the minimal\
      \ required tooling to support that. Once you\u2019ve provided the value, roll\
      \ it out some more and keep iterating on the tooling.\nAlternatively, you could\
      \ attempt a large scale migration to data contracts, but there\u2019s a lot\
      \ of potential challenges there (speaking from experience \U0001F605). You\u2019\
      d need strong exec buy-in, which might not be so difficult if your organisation\
      \ has a strategy that depends on quality data, and if you can articulate how\
      \ data contracts helps with that. But, even with that you\u2019re going to need\
      \ to have many teams prioritise a lot of work, and there\u2019s going to be\
      \ push back. They have other things to do, and their incentives may favour prioritising\
      \ that work instead.\nSo I\u2019d recommend the first, gradual approach. You\u2019\
      re not just rolling out some new tooling - your changing your data culture to\
      \ one where data generators take more responsibility and provide quality data\
      \ to consumers in order to drive business value from data. That\u2019s going\
      \ to take some time! So be patient, target high value use cases and projects,\
      \ and keep at it \U0001F642"
  - name: Hrithik Kumar
    text: Really appreciate your response.
  - name: Hrithik Kumar
    text: How do you see the concept of data contracts adapting to emerging trends
      in data privacy and regulations, such as GDPR(General Data Protection Regulation)
      and data sovereignty? Are there specific considerations that organizations need
      to keep in mind when implementing data contracts in such a regulatory landscape?
  - name: Andrew Jones
    text: "That\u2019s an very important question. Regulation in tech in general,\
      \ and data in particular, is only going to get stronger, so it\u2019s something\
      \ we should all be thinking about more!\nWith data contracts, we have the perfect\
      \ place to categorise and define other metadata about the data. For example,\
      \ in [our implementation at GoCardless](https://medium.com/gocardless-tech/implementing-data-contracts-at-gocardless-3b5c49074d13)\
      \ each field definition contains metadata telling us the type of data, whether\
      \ it is personal data, an identifier, and how to anonymise it:\n```field(\n\
      \ 'bank_account_id',\n 'Unique identifier for a specific bank account, following\
      \ the standard GC ID format.',\n data_types.string,\n field_category.gocardless_internal,\n\
      \ is_personal_data.yes,\n personal_data_identifier.indirect,\n field_anonymisation_strategy.none,\n\
      \ required=true,\n),```\nThat then makes it very easy to build tooling that\
      \ can automate your compliance to the regulations. In our case, we have a data\
      \ handling service that takes care of anonymisation and deletion as required\
      \ by GDPR. We also use this metadata to automate access controls. In future,\
      \ we could extend this metadata to help us build tooling to ensure data sovereignty,\
      \ define how we process the data if it\u2019s used for AI training, etc.\nThe\
      \ great thing about this tooling is it doesn\u2019t care _how_ the data is structured.\
      \ The schema could be wide with lots of fields, or deep with lots of nesting\
      \ - it doesn\u2019t matter. The data generator has full autonomy over that,\
      \ and as long as they categorise the data correctly, our tooling with work with\
      \ that data and do the right thing to ensure compliance, _without_ the data\
      \ generator becoming an expert in GDPR!"
  - name: Hrithik Kumar
    text: Thanks Andrew Jones for sharing your thoughts on this topic.
- name: Toxicafunk
  text: What are the most common mistakes you've seen even defining data contracts?
    What would be the top 3 or 5 things to avoid?
  replies:
  - name: Andrew Jones
    text: "Hey, good question!\nI\u2019d say:\n1. Focussing on the tech but not the\
      \ people/culture side. It\u2019s really all about the people and changing how\
      \ we _do_ data, and the tech is there to support that\n2. Trying to apply data\
      \ contracts to everything, all at once! You need to manage that migration, focussing\
      \ on where the most value is first\n3. Making it too complicated. It\u2019s\
      \ a very simple idea really, so don\u2019t over complicate it! Build the appropriate\
      \ amount of tooling, automate where you can, put in place just enough process,\
      \ but no more.\nHope that helps \U0001F642"
  - name: Toxicafunk
    text: Really helpful yes,  thanks for being here!
- name: Sven
  text: 'Thanks!

    What are good tools or tech-stack to implement Data Contracts? And do we want
    the Ownership on the IT or Biz side? For example a yml file in a git repo vs nice
    UI to change a schema.'
  replies:
  - name: Andrew Jones
    text: "Hey Sven, thanks for the question!\nI like implementing data contracts\
      \ at the infrastructure layer. That allows you to guarantee that (say) your\
      \ BigQuery table will always match the contract, as it is generated from it.\
      \ There\u2019s a sample implementation in my book showing data contracts implemented\
      \ using [Pulumi](https://www.pulumi.com), an open source infrastructure as code\
      \ tool.\nThe tooling is best owned by a dedicated infrastructure or data infrastructure\
      \ team, and should be designed so it allows the contracts to be owned by whichever\
      \ team is generating the data.\nOften that is a product engineering team, so\
      \ the ability to define the contract in yml in a git repo is a good option,\
      \ but more generally, it should be where it would most expect to be. For example,\
      \ at GoCardless where I work we used [Jsonnet](https://jsonnet.org) rather than\
      \ yml, as all our other infrastructure is defined in Jsonnet, so it just made\
      \ sense to be consistent. But there is nothing about Jsonnet that makes it better\
      \ than yml for defining data contracts, so I wouldn\u2019t recommend it to an\
      \ organisation that doesn\u2019t already use it.\nIf you\u2019re targeting non-engineering\
      \ teams, then a nice UI might make more sense. I haven\u2019t heard of anyone\
      \ building those internally in their organisations as yet, but some offerings\
      \ that do offer a nice UI are [https://datamesh-manager.com](https://datamesh-manager.com)\
      \ and [https://docs.soda.io/soda-cloud/agreements.html](https://docs.soda.io/soda-cloud/agreements.html).\n\
      Hope that makes sense \U0001F642 Let me know if you have any follow up questions\
      \ or would like something clarified!"
  - name: Sven
    text: Wow, thanks for the detailed answer! I'll have a look into this tools!
- name: Sandeep
  text: "Does the book talk about the local development loop for the engineer ? \n\
    Also how do separate teams test out changes before pushing to prod ? \nThanks\
    \ for your time on these questions :)"
  replies:
  - name: Andrew Jones
    text: "Hey Sandeep, good questions!\nI do a little, but at a higher level and\
      \ not in loads of detail.\nI talk about how CI checks can help, how to use tools\
      \ like JSON Schema and make use of existing open source libraries. I also talk\
      \ about managing schema evolution in quite a bit of detail.\nBut mostly, I\u2019\
      m talking about the patterns that help you implement data contracts in your\
      \ organisation, rather than exactly how to do so in any particular language/service."
  - name: Sandeep
    text: 'Thank you

      The schema evolution and the patterns seem super cool'
- name: Sandeep
  text: "More general question, do these contracts stay in a common repository or\
    \ go in each pipeline repo. ? \nIgnore, if this is too specific"
  replies:
  - name: Andrew Jones
    text: "I think data contracts should be in the place your data generators most\
      \ expect them to be.\nIf their software/product engineers, then that should\
      \ be probably be where they manage related things like their REST APIs, infrastructure,\
      \ etc.\nFor some organisations that will be a common monorepo, for others that\
      \ will be in the repo specific for their service. A data contract most likely\
      \ belongs to a _service_, so should live there. (_Service_ should be a broad\
      \ definition, so would include pipelines)\nHaving said that, having a common\
      \ place to _query_ each data contract is very useful for tooling, discovery,\
      \ etc. That could be a schema registry, a data catalog (with a good API), etc.\n\
      Hope that helps! Let me know if you have any follow-up questions \U0001F642"
- name: Toxicafunk
  text: 'In the free chapter (ch. 1) you mention the lack of expectations, reliability
    and autonomy as the main problems a data contract should address.

    1. it seems most of these problems are at least partially addressed by a data
    mesh architecture,  Does your book discuss `Data Contracts` as a part of a Data
    Mesh initiative or do you consider contracts by themselves enough to address them?

    2. Should a `data contracts` also address the `why` we care about exposing a given
    field or should the `why` be addressed at the scope of pipelines instead of fields?'
  replies:
  - name: Andrew Jones
    text: "Hey Toxicafunk,\n1. \nYes, there\u2019s a section in chapter 2 titled _Data\
      \ contracts and the data mesh_ that aims to answer that \U0001F642 In short,\
      \ they are very much complimentary, and data mesh is one of the inspirations\
      \ behind data contracts.\nI believe it would be very hard to implement a data\
      \ mesh without data contracts. On the flip side, you can certainly use data\
      \ contracts without committing to a full data mesh architecture.\n2.\nThat\u2019\
      s a great question! I think the why should be captured in the contract. There\
      \ is a reason that field was exposed, and documenting that would help others\
      \ know what that field is useful for.\nIf not in the data contract, it might\
      \ instead be in a requirements document or similar, but they tend to go out\
      \ of date. The data contract will be maintained for as long as the data is.\n\
      I love this question though. Always _start with why_!"
- name: Kathryn Armitstead
  text: Are data contracts the sort of concept that one could introduce to an organisation
    gradually, eg across 2 teams and then aim to get buy-in from other teams, or is
    to something that needs general buy-in to be effective? I like what I've heard
    about them, but finding how to introduce into a very busy organisation with lots
    of other priorities Would be a big challenge.
  replies:
  - name: Andrew Jones
    text: "Kathryn Armitstead great question!\nI think you can do so gradually. Focus\
      \ on where they add most value, start introducing the language and showing how\
      \ they help. Build the minimal tooling to support that. Then go from there.\n\
      I talk a lot about this in chapter 3, _How to Get Adoption in Your Organization._\n\
      As you say, getting this prioritised in an organization will be a big challenge.\
      \ You need to be able to articulate the _value_ of it, and the value of data\
      \ in general. Then once you\u2019ve done that, you need to align the adoption\
      \ of data contracts with the _incentives_ of the teams you\u2019re asking to\
      \ prioritise.\nBut this shouldn\u2019t put you off! Often, I see people say\
      \ \u201Cthere\u2019s no way this will be prioritised\u201D, but there is! Software\
      \ engineers, product managers, directors, etc will care about data quality if\
      \ they understand the issues being caused, the cost of those issues, and the\
      \ value from being better \U0001F642"
  - name: Kathryn Armitstead
    text: great answer - thanks Andrew Jones . I love the option of being able to
      progress with minimal tooling to demonstrate value and get buy-in.
- name: Sven
  text: What are the big differences between a Data Contract and a Data Catalog? I
    just saw different definitions. Is it possible to combine them?
  replies:
  - name: Andrew Jones
    text: "Hey Sven, I\u2019d say they\u2019re quite different, but related.\nA data\
      \ catalog is a great tool for discovering the data you have, but they don\u2019\
      t do much more than that.\nA data contract is _how_ that data is being generated\
      \ and managed.\nA data contract will include the schema, some documentation,\
      \ the owner, SLOs, etc. These are all things you would want in your data catalog,\
      \ and we populate our data catalog from the data contract.\nI talk a bit about\
      \ data catalogs and data contracts in chapter 9."
  - name: Sven
    text: Perfect, thanks!

---

Despite the passage of time and the evolution of technology and architecture, the challenges we face in building data platforms persist. Our data often remains unreliable, lacks trust, and fails to deliver the promised value. With Driving Data Quality with Data Contracts, you’ll discover the potential of data contracts to transform how you build your data platforms, finally overcoming these enduring problems. You’ll learn how establishing contracts as the interface allows you to explicitly assign responsibility and accountability of the data to those who know it best—the data generators—and give them the autonomy to generate and manage data as required. The book will show you how data contracts ensure that consumers get quality data with clearly defined expectations, enabling them to build on that data with confidence to deliver valuable analytics, performant ML models, and trusted data-driven products. By the end of this book, you’ll have gained a comprehensive understanding of how data contracts can revolutionize your organization’s data culture and provide a competitive advantage by unlocking the real value within your data.