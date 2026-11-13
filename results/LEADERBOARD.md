# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 225 windows, 5880 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 582 | 56.0 | 52.8 | $+186.34 | +3.2% | $1186.34 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 457 | 54.7 | 52.5 | $+46.78 | +1.0% | $1046.78 | +0.2 | done | can't tell from luck |
| value_ev20 | 109 | 33.9 | 37.0 | $-135.89 | -12.5% | $864.11 | -1.0 | Sun 6:45 AM | too few trades (109/200) |
| value_ev10 | 292 | 37.7 | 41.0 | $-341.85 | -11.7% | $658.15 | -1.7 | done | can't tell from luck |
| trend_filter | 303 | 44.9 | 50.1 | $-422.79 | -14.0% | $577.21 | -2.5 | done | losing for real |
| value_ev5 | 422 | 39.6 | 42.7 | $-462.74 | -11.0% | $537.26 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 892 | 50.4 | 51.5 | $-520.47 | -5.8% | $479.53 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 457 | 45.3 | 49.7 | $-580.16 | -12.7% | $419.84 | -2.8 | done | losing for real |
| coinflip | 892 | 49.4 | 51.0 | $-625.78 | -7.0% | $374.22 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 582 | 44.0 | 49.6 | $-855.62 | -14.7% | $144.38 | -3.6 | done | losing for real |
| always_up | 892 | 47.1 | 50.3 | $-925.53 | -10.4% | $74.47 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1318 | 46.4 | 49.7 | $-1298.29 |
| ETH | 1462 | 46.6 | 49.0 | $-1390.51 |
| SOL | 1518 | 47.9 | 49.4 | $-1244.11 |
| XRP | 1582 | 49.2 | 49.2 | $-704.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
