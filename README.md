# codemapper
Semantic, relational and hierarchical code indexing aided by summaries

## Concept

### Context Generation Process
```mermaid
graph TD
    StartIndexing[Start: Index File] --> IdentifyElements{Identify Elements}
    IdentifyElements -->|const| SummarizeConstant[Summarize Const]
    IdentifyElements -->|var| SummarizeVariable[Summarize Var]
    IdentifyElements -->|function| SummarizeFunction[Summarize Function]
    IdentifyElements -->|class| SummarizeClass[Summarize Class]
    SummarizeFunction -->|Sub Functions| SummarizeFunction
    SummarizeClass -->|Methods| SummarizeMethods[Summarize Methods]
    SummarizeMethods --> ClassSummary[Class Summary]
    SummarizeConstant --> FileSummary[File Summary]
    SummarizeVariable --> FileSummary
    SummarizeFunction --> FileSummary
    ClassSummary --> FileSummary
    FileSummary --> PackageSummary[Package Summary]
```

### Relationships between Summaries
```mermaid
graph TD
    PackageSummary[Package Summary] --> FileSummary[File Summary]
    FileSummary --> ConstantSummary[Constant Summary]
    FileSummary --> VariableSummary[Variable Summary]
    FileSummary --> FunctionSummary[Function Summary]
    FileSummary --> ClassSummary[Class Summary]
    FunctionSummary --> SubFunctionSummary[Sub-Function Summary]
    ClassSummary --> MethodSummary[Method Summary]
    SubFunctionSummary --> SubSubFunction[Sub-Sub-Function Summary]
    SubSubFunction --> SubSubSubFunction[Sub-Sub-Sub-Function Summary]
    MethodSummary --> SubMethodSummary[Sub-Method Summary]

```

### Cross-file relationships

Further context needs to be built often to understand how some constants, functions are being used....

```mermaid
graph LR
    SummarizeConstant[Summarize Const] --> LookupUsage[Lookup Usages] --> CompilePurpose
```

### Tree-possiblity

Could the index be a tree-like structure... where the context gets smaller and smaller as you go down,
and stays limited to the scope of classes, functions... whatever is "selected"... and that's it...
