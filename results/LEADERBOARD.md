# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 966 windows, 26752 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 494 | 34.8 | 34.9 | $-199.50 | -4.0% | $800.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2730 | 51.4 | 50.5 | $-667.56 | -2.4% | $332.44 | -1.3 | done | can't tell from luck |
| value_ev10 | 1220 | 38.0 | 39.1 | $-699.76 | -5.7% | $300.24 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2280 | 50.1 | 49.7 | $-914.09 | -4.0% | $85.91 | -1.9 | done | can't tell from luck |
| trend_filter | 1600 | 49.9 | 50.9 | $-1065.98 | -6.7% | $-65.98 | -2.7 | done | losing for real |
| value_ev5 | 1850 | 39.8 | 41.0 | $-1080.59 | -5.8% | $-80.59 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2280 | 49.9 | 51.0 | $-1579.74 | -6.9% | $-579.74 | -3.4 | done | losing for real |
| coinflip | 3856 | 50.2 | 50.4 | $-1728.42 | -4.5% | $-728.42 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 3856 | 50.9 | 51.6 | $-1968.95 | -5.1% | $-968.95 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2730 | 48.6 | 50.3 | $-1980.32 | -7.3% | $-980.32 | -3.8 | done | losing for real |
| always_up | 3856 | 46.9 | 49.6 | $-3769.88 | -9.8% | $-2769.88 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6093 | 48.2 | 49.0 | $-3482.76 |
| ETH | 6646 | 48.1 | 48.5 | $-4135.52 |
| SOL | 6989 | 48.3 | 48.6 | $-3794.38 |
| XRP | 7024 | 48.2 | 48.5 | $-4242.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
