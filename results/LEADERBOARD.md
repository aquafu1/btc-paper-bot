# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 286 windows, 7561 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 744 | 54.2 | 51.7 | $+14.04 | +0.2% | $1014.04 | +0.1 | done | can't tell from luck |
| value_ev20 | 140 | 35.0 | 36.4 | $-129.35 | -9.2% | $870.65 | -0.9 | Sun 4:00 AM | too few trades (140/200) |
| reversal_60m_0.30pct | 608 | 52.3 | 51.8 | $-207.75 | -3.4% | $792.25 | -0.9 | done | can't tell from luck |
| value_ev10 | 367 | 38.1 | 40.5 | $-365.03 | -9.9% | $634.97 | -1.6 | done | can't tell from luck |
| trend_filter | 401 | 46.9 | 50.4 | $-465.60 | -11.6% | $534.40 | -2.4 | done | losing for real |
| value_ev5 | 541 | 39.9 | 42.1 | $-523.56 | -9.7% | $476.44 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 608 | 47.7 | 49.8 | $-556.39 | -9.2% | $443.61 | -2.3 | done | losing for real |
| coinflip | 1136 | 49.9 | 50.9 | $-700.93 | -6.2% | $299.07 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1136 | 49.6 | 51.5 | $-875.09 | -7.7% | $124.91 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 744 | 45.8 | 49.9 | $-919.74 | -12.4% | $80.26 | -3.4 | done | losing for real |
| always_up | 1136 | 47.4 | 50.2 | $-1108.59 | -9.8% | $-108.59 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1683 | 46.8 | 49.4 | $-1581.66 |
| ETH | 1889 | 47.2 | 48.8 | $-1715.58 |
| SOL | 1965 | 48.2 | 49.3 | $-1539.83 |
| XRP | 2024 | 48.9 | 49.0 | $-1000.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
