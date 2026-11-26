# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1435 windows, 36596 settled trades, 445 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 738 | 34.6 | 35.3 | $-513.47 | -7.0% | $486.53 | -1.4 | done | can't tell from luck |
| value_ev10 | 1778 | 38.8 | 39.1 | $-801.03 | -4.5% | $198.97 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3653 | 50.9 | 50.1 | $-973.65 | -2.7% | $26.35 | -1.6 | done | can't tell from luck |
| value_ev5 | 2680 | 40.6 | 41.1 | $-1285.48 | -4.8% | $-285.48 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3070 | 49.2 | 49.3 | $-1508.96 | -4.9% | $-508.96 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3070 | 50.8 | 51.0 | $-1581.05 | -5.2% | $-581.05 | -2.9 | done | losing for real |
| trend_filter | 2174 | 48.5 | 50.3 | $-1900.11 | -8.7% | $-900.11 | -4.2 | done | losing for real |
| coinflip | 5260 | 50.1 | 50.0 | $-2201.42 | -4.2% | $-1201.42 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3653 | 49.1 | 50.2 | $-2277.03 | -6.2% | $-1277.03 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5260 | 50.1 | 51.3 | $-3283.72 | -6.2% | $-2283.72 | -4.7 | done | losing for real |
| always_up | 5260 | 48.0 | 49.2 | $-3596.56 | -6.8% | $-2596.56 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9294 | 48.1 | 48.7 | $-4866.13 |
| ETH | 9992 | 48.0 | 48.0 | $-5472.12 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
