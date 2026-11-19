# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 760 windows, 20955 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2141 | 51.4 | 50.6 | $-535.16 | -2.5% | $464.84 | -1.2 | done | can't tell from luck |
| value_ev10 | 960 | 37.9 | 39.1 | $-627.58 | -6.5% | $372.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1771 | 50.0 | 49.6 | $-664.91 | -3.8% | $335.09 | -1.6 | done | can't tell from luck |
| trend_filter | 1233 | 49.9 | 50.9 | $-801.88 | -6.5% | $198.12 | -2.3 | done | losing for real |
| value_ev5 | 1447 | 40.2 | 41.1 | $-826.64 | -5.7% | $173.36 | -1.8 | done | can't tell from luck |
| coinflip | 3032 | 50.4 | 50.3 | $-1156.60 | -3.8% | $-156.60 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1771 | 50.0 | 51.2 | $-1236.22 | -7.0% | $-236.22 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2141 | 48.6 | 50.2 | $-1542.82 | -7.2% | $-542.82 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3032 | 50.8 | 51.7 | $-1644.33 | -5.4% | $-644.33 | -3.1 | done | losing for real |
| always_up | 3032 | 47.0 | 49.7 | $-2852.13 | -9.4% | $-1852.13 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4753 | 48.1 | 49.1 | $-2971.66 |
| ETH | 5225 | 48.0 | 48.6 | $-3443.41 |
| SOL | 5455 | 48.0 | 48.6 | $-3278.39 |
| XRP | 5522 | 48.6 | 48.5 | $-2496.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
