# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 482 windows, 13236 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 241 | 35.3 | 35.9 | $-112.29 | -4.7% | $887.71 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1123 | 50.9 | 49.8 | $-190.32 | -1.7% | $809.68 | -0.6 | done | can't tell from luck |
| value_ev10 | 622 | 39.2 | 40.1 | $-323.65 | -5.2% | $676.35 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1336 | 50.1 | 50.0 | $-414.88 | -3.1% | $585.12 | -1.1 | done | can't tell from luck |
| value_ev5 | 919 | 41.1 | 41.8 | $-451.19 | -4.9% | $548.81 | -1.3 | done | can't tell from luck |
| trend_filter | 773 | 49.4 | 50.8 | $-511.15 | -6.6% | $488.85 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1336 | 49.9 | 51.5 | $-950.47 | -7.1% | $49.53 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1123 | 49.1 | 51.5 | $-996.00 | -8.9% | $4.00 | -3.0 | done | losing for real |
| coinflip | 1921 | 49.9 | 50.8 | $-1011.95 | -5.3% | $-11.95 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1921 | 49.6 | 51.7 | $-1445.83 | -7.5% | $-445.83 | -3.4 | done | losing for real |
| always_up | 1921 | 46.4 | 50.5 | $-2241.89 | -11.7% | $-1241.89 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2985 | 47.4 | 49.3 | $-2352.62 |
| ETH | 3315 | 48.1 | 48.9 | $-2097.48 |
| SOL | 3452 | 47.8 | 49.3 | $-2434.00 |
| XRP | 3484 | 48.5 | 49.0 | $-1765.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
