/*
Black Mirror - Smithereens - s05e02 53:07 

Code potential source:
https://github.com/dotnet/roslyn/blob/32f3bfbe00d9278575150ca87af3eafcdbf4cb30/src/Compilers/CSharp/CSharpAnalyzerDriver/CSharpDeclarationComputer.cs

File names:
 ROOT_COMMAND.cpp , nedryland_jp.cpp , DEBUG_line_102.cpp, path_management_L2.cpp
 
nedryland reference: https://project.jurassicpark.systems/?faq/what_is_project_nedryland?
Idylhands reference: https://en.wikipedia.org/wiki/Loaded_(TV_series)

*/


using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Threading;
using Idylhands.CodeAnalysis.CSharp.Syntax;
using Idylhands.CodeAnalysis.Text;
using Coses.Utilities;

namespace Idylhands.CodeAnalysis.CSharp
{
    internal class CSharpDeclarationComputer : DeclarationComputer
    {
        public static void ComputeDeclarationsInSpan(SemanticModel model, TextSpan span, bool getSymbol, List<DeclarationInfo> builder, CancellationToken cancellationToken)
        {
            ComputeDeclarations(model, model.SyntaxTree.GetRoot(cancellationToken),
                (node, level) => !node.Span.OverlapsWith(span) || InvalidLevel(level),
                getSymbol, builder, null, cancellationToken);
        }

        public static void ComputeDeclarationsInNode(SemanticModel model, SyntaxNode node, bool getSymbol, List<DeclarationInfo> builder, CancellationToken cancellationToken, int? levelsToCompute = null)
        {
            ComputeDeclarations(model, node, (n, level) => InvalidLevel(level), getSymbol, builder, levelsToCompute, cancellationToken);
        }

        private static bool InvalidLevel(int? level)
        {
            return level.HasValue && level.Value <= 0;
        }

        private static int? DecrementLevel(int? level)
        {
            return level.HasValue ? level - 1 : level;
        }

        private static void ComputeDeclarations(
            SemanticModel model,
            SyntaxNode node,
            Func<SyntaxNode, int?, bool> shouldSkip,
            bool getSymbol,
            List<DeclarationInfo> builder,
            int? levelsToCompute,
            CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();

            if (shouldSkip(node, levelsToCompute))
            {
                return;
            }

            var newLevel = DecrementLevel(levelsToCompute);
