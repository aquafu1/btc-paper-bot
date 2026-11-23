# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1237 windows, 33725 settled trades, 430 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 663 | 34.2 | 35.3 | $-504.16 | -7.6% | $495.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1615 | 38.6 | 39.2 | $-810.67 | -5.0% | $189.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3382 | 50.8 | 50.3 | $-1071.71 | -3.2% | $-71.71 | -1.8 | done | can't tell from luck |
| value_ev5 | 2440 | 40.4 | 41.1 | $-1277.46 | -5.2% | $-277.46 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2827 | 49.5 | 49.4 | $-1279.75 | -4.5% | $-279.75 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2827 | 50.5 | 51.1 | $-1677.47 | -5.9% | $-677.47 | -3.2 | done | losing for real |
| trend_filter | 1994 | 48.7 | 50.4 | $-1680.11 | -8.4% | $-680.11 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3382 | 49.2 | 50.2 | $-2109.51 | -6.2% | $-1109.51 | -3.7 | done | losing for real |
| coinflip | 4865 | 50.0 | 50.1 | $-2207.54 | -4.5% | $-1207.54 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4865 | 50.2 | 51.4 | $-2976.17 | -6.1% | $-1976.17 | -4.4 | done | losing for real |
| always_up | 4865 | 47.8 | 49.3 | $-3582.79 | -7.4% | $-2582.79 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7894 | 48.0 | 48.9 | $-4586.87 |
| ETH | 8521 | 48.1 | 48.3 | $-5006.24 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
