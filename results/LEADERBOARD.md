# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 416 windows, 11437 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 980 | 50.8 | 50.1 | $-267.89 | -2.7% | $732.11 | -0.9 | done | can't tell from luck |
| value_ev10 | 535 | 39.8 | 40.4 | $-271.49 | -5.1% | $728.51 | -1.0 | done | can't tell from luck |
| value_ev5 | 804 | 41.8 | 42.1 | $-370.32 | -4.6% | $629.68 | -1.1 | done | can't tell from luck |
| trend_filter | 657 | 49.9 | 50.8 | $-372.59 | -5.7% | $627.41 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1152 | 49.4 | 49.9 | $-544.65 | -4.7% | $455.35 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1152 | 50.6 | 51.8 | $-750.90 | -6.5% | $249.10 | -2.3 | done | losing for real |
| coinflip | 1656 | 50.2 | 50.9 | $-830.49 | -5.0% | $169.51 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 980 | 49.2 | 51.8 | $-891.12 | -9.1% | $108.88 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1656 | 49.7 | 51.6 | $-1181.20 | -7.1% | $-181.20 | -3.0 | done | losing for real |
| always_up | 1656 | 45.8 | 50.6 | $-2158.07 | -13.0% | $-1158.07 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2588 | 47.7 | 49.4 | $-1884.69 |
| ETH | 2877 | 47.9 | 49.0 | $-1819.09 |
| SOL | 2961 | 47.7 | 49.5 | $-2439.28 |
| XRP | 3011 | 48.8 | 49.3 | $-1652.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
