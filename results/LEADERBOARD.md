# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 164 windows, 4197 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 308 | 59.7 | 53.2 | $+308.34 | +10.0% | $1308.34 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 406 | 56.9 | 52.6 | $+230.11 | +5.7% | $1230.11 | +1.2 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 6:15 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 649 | 52.1 | 51.1 | $-129.12 | -2.0% | $870.88 | -0.5 | done | can't tell from luck |
| value_ev10 | 214 | 38.8 | 40.9 | $-211.47 | -9.9% | $788.53 | -1.3 | done | can't tell from luck |
| value_ev5 | 314 | 39.8 | 42.6 | $-331.73 | -10.6% | $668.27 | -1.7 | done | can't tell from luck |
| coinflip | 649 | 50.1 | 50.9 | $-380.46 | -5.9% | $619.54 | -1.5 | done | can't tell from luck |
| trend_filter | 216 | 40.7 | 48.9 | $-419.61 | -19.4% | $580.39 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 308 | 40.3 | 49.0 | $-632.13 | -20.5% | $367.87 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 406 | 43.1 | 49.6 | $-643.26 | -15.8% | $356.74 | -3.2 | done | losing for real |
| always_up | 649 | 46.4 | 50.1 | $-749.27 | -11.5% | $250.73 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 917 | 46.1 | 49.4 | $-825.96 |
| ETH | 1045 | 45.8 | 48.9 | $-1108.61 |
| SOL | 1099 | 48.0 | 48.9 | $-836.74 |
| XRP | 1136 | 50.4 | 49.1 | $-269.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
