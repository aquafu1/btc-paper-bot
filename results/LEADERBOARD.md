# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 581 windows, 16082 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1364 | 51.1 | 49.6 | $-257.90 | -1.9% | $742.10 | -0.7 | done | can't tell from luck |
| value_ev20 | 316 | 32.9 | 35.2 | $-374.56 | -11.9% | $625.44 | -1.6 | done | can't tell from luck |
| trend_filter | 933 | 50.4 | 50.9 | $-514.48 | -5.5% | $485.52 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1635 | 51.1 | 51.0 | $-749.56 | -4.6% | $250.44 | -1.9 | done | can't tell from luck |
| value_ev10 | 757 | 37.3 | 39.4 | $-757.94 | -10.0% | $242.06 | -2.3 | done | losing for real |
| value_ev5 | 1130 | 39.8 | 41.3 | $-887.70 | -7.9% | $112.30 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1635 | 48.9 | 49.9 | $-1022.66 | -6.3% | $-22.66 | -2.5 | done | losing for real |
| coinflip | 2316 | 49.9 | 50.5 | $-1236.14 | -5.3% | $-236.14 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1364 | 48.9 | 51.3 | $-1308.69 | -9.6% | $-308.69 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2316 | 50.2 | 51.8 | $-1632.67 | -7.0% | $-632.67 | -3.5 | done | losing for real |
| always_up | 2316 | 47.0 | 49.9 | $-2339.83 | -10.1% | $-1339.83 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3649 | 47.8 | 49.2 | $-2705.22 |
| ETH | 4012 | 47.9 | 48.6 | $-2783.82 |
| SOL | 4181 | 47.7 | 48.8 | $-3209.39 |
| XRP | 4240 | 48.4 | 48.6 | $-2383.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
