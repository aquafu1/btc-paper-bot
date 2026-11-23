# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1203 windows, 33181 settled trades, 136 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 647 | 34.6 | 35.3 | $-418.79 | -6.5% | $581.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1584 | 38.6 | 39.2 | $-810.46 | -5.1% | $189.54 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3325 | 50.8 | 50.3 | $-1086.11 | -3.3% | $-86.11 | -1.9 | done | can't tell from luck |
| value_ev5 | 2395 | 40.4 | 41.1 | $-1249.26 | -5.2% | $-249.26 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2779 | 49.6 | 49.4 | $-1255.79 | -4.5% | $-255.79 | -2.4 | done | losing for real |
| trend_filter | 1959 | 48.7 | 50.5 | $-1670.37 | -8.5% | $-670.37 | -3.9 | done | losing for real |
| reversal_60m_0.30pct | 2779 | 50.4 | 51.1 | $-1685.99 | -6.1% | $-685.99 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3325 | 49.2 | 50.2 | $-2052.20 | -6.2% | $-1052.20 | -3.6 | done | losing for real |
| coinflip | 4796 | 50.1 | 50.1 | $-2135.92 | -4.5% | $-1135.92 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4796 | 50.2 | 51.4 | $-2949.09 | -6.1% | $-1949.09 | -4.4 | done | losing for real |
| always_up | 4796 | 47.9 | 49.3 | $-3453.51 | -7.2% | $-2453.51 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7627 | 48.1 | 48.9 | $-4260.64 |
| ETH | 8244 | 48.1 | 48.4 | $-4922.62 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
