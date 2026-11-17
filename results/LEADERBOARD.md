# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 637 windows, 17616 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1490 | 51.1 | 49.6 | $-188.24 | -1.3% | $811.76 | -0.5 | done | can't tell from luck |
| value_ev20 | 331 | 33.8 | 35.3 | $-284.70 | -8.6% | $715.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1019 | 50.4 | 50.8 | $-518.85 | -5.1% | $481.15 | -1.7 | done | can't tell from luck |
| value_ev10 | 810 | 38.3 | 39.5 | $-589.42 | -7.3% | $410.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1229 | 40.7 | 41.4 | $-713.75 | -5.8% | $286.25 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1812 | 50.9 | 51.0 | $-799.36 | -4.4% | $200.64 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1812 | 49.1 | 50.0 | $-1040.98 | -5.7% | $-40.98 | -2.5 | done | losing for real |
| coinflip | 2541 | 50.1 | 50.5 | $-1196.65 | -4.7% | $-196.65 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1490 | 48.9 | 51.4 | $-1412.68 | -9.5% | $-412.68 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2541 | 50.6 | 51.7 | $-1414.29 | -5.6% | $-414.29 | -2.9 | done | losing for real |
| always_up | 2541 | 47.3 | 49.7 | $-2260.03 | -8.9% | $-1260.03 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4000 | 48.3 | 49.3 | $-2418.89 |
| ETH | 4415 | 48.3 | 48.6 | $-2594.10 |
| SOL | 4569 | 48.0 | 48.8 | $-3026.73 |
| XRP | 4632 | 48.4 | 48.6 | $-2379.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
