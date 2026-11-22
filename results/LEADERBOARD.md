# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1069 windows, 29586 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 553 | 34.4 | 35.1 | $-343.30 | -6.2% | $656.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2998 | 51.4 | 50.5 | $-691.69 | -2.3% | $308.31 | -1.3 | done | can't tell from luck |
| value_ev10 | 1367 | 37.6 | 39.2 | $-980.20 | -7.2% | $19.80 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2512 | 49.7 | 49.6 | $-1154.93 | -4.6% | $-154.93 | -2.3 | done | losing for real |
| trend_filter | 1759 | 49.5 | 50.7 | $-1278.73 | -7.3% | $-278.73 | -3.1 | done | losing for real |
| value_ev5 | 2077 | 39.6 | 41.0 | $-1382.07 | -6.7% | $-382.07 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2512 | 50.3 | 51.0 | $-1586.19 | -6.3% | $-586.19 | -3.2 | done | losing for real |
| coinflip | 4270 | 50.5 | 50.3 | $-1710.88 | -4.0% | $-710.88 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4270 | 51.0 | 51.5 | $-2079.98 | -4.9% | $-1079.98 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2998 | 48.6 | 50.3 | $-2196.24 | -7.3% | $-1196.24 | -4.1 | done | losing for real |
| always_up | 4270 | 47.3 | 49.4 | $-3749.80 | -8.8% | $-2749.80 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6752 | 48.4 | 49.0 | $-3459.56 |
| ETH | 7316 | 48.1 | 48.5 | $-4640.47 |
| SOL | 7720 | 48.1 | 48.5 | $-4500.00 |
| XRP | 7798 | 48.3 | 48.3 | $-4553.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
