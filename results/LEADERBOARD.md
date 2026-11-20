# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 905 windows, 24961 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1140 | 38.2 | 39.1 | $-611.46 | -5.4% | $388.54 | -1.5 | done | can't tell from luck |
| value_ev5 | 1727 | 40.0 | 41.0 | $-995.84 | -5.8% | $4.16 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2110 | 49.8 | 49.8 | $-1006.09 | -4.8% | $-6.09 | -2.2 | done | losing for real |
| trend_filter | 1480 | 49.9 | 51.0 | $-1034.64 | -7.0% | $-34.64 | -2.8 | done | losing for real |
| reversal_15m_0.10pct | 2547 | 50.5 | 50.5 | $-1048.40 | -4.1% | $-48.40 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2110 | 50.2 | 50.9 | $-1309.95 | -6.2% | $-309.95 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2547 | 49.5 | 50.4 | $-1357.82 | -5.3% | $-357.82 | -2.7 | done | losing for real |
| coinflip | 3612 | 50.2 | 50.3 | $-1616.27 | -4.5% | $-616.27 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3612 | 51.2 | 51.7 | $-1687.87 | -4.7% | $-687.87 | -2.9 | done | losing for real |
| always_up | 3612 | 46.9 | 49.6 | $-3550.97 | -9.8% | $-2550.97 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5690 | 48.3 | 49.1 | $-3105.74 |
| ETH | 6206 | 48.2 | 48.6 | $-3760.95 |
| SOL | 6513 | 48.2 | 48.6 | $-3738.18 |
| XRP | 6552 | 48.3 | 48.5 | $-3715.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
