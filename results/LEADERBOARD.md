# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 83 windows, 2114 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 327 | 56.9 | 50.9 | $+283.85 | +8.7% | $1283.85 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 153 | 58.8 | 52.8 | $+139.22 | +9.1% | $1139.22 | +1.2 | Wed 6:15 PM | too few trades (153/200) |
| reversal_15m_0.10pct | 201 | 56.2 | 52.1 | $+119.14 | +5.9% | $1119.14 | +0.9 | done | can't tell from luck |
| value_ev10 | 114 | 43.0 | 40.1 | $+16.88 | +1.5% | $1016.88 | +0.1 | Thu 3:15 AM | too few trades (114/200) |
| trend_filter | 114 | 48.2 | 48.7 | $-43.05 | -3.8% | $956.95 | -0.4 | Thu 3:15 AM | too few trades (114/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 2:45 PM | too few trades (43/200) |
| value_ev5 | 154 | 41.6 | 41.5 | $-68.55 | -4.5% | $931.45 | -0.5 | Wed 6:00 PM | too few trades (154/200) |
| coinflip | 327 | 50.5 | 51.5 | $-170.09 | -5.2% | $829.91 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 153 | 41.2 | 48.7 | $-271.39 | -17.7% | $728.61 | -2.2 | Wed 6:15 PM | too few trades (153/200) |
| momentum_15m_0.10pct | 201 | 43.8 | 49.5 | $-283.18 | -14.1% | $716.82 | -2.0 | done | can't tell from luck |
| always_up | 327 | 47.1 | 50.1 | $-292.16 | -8.9% | $707.84 | -1.6 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 456 | 48.5 | 49.8 | $-74.10 |
| ETH | 507 | 47.7 | 48.6 | $-158.73 |
| SOL | 567 | 50.4 | 48.4 | $-114.95 |
| XRP | 584 | 50.0 | 48.5 | $-275.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
