# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1224 windows, 33521 settled trades, 435 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 653 | 34.5 | 35.3 | $-453.45 | -6.9% | $546.55 | -1.4 | done | can't tell from luck |
| value_ev10 | 1601 | 38.8 | 39.2 | $-756.99 | -4.7% | $243.01 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3361 | 50.8 | 50.3 | $-1089.17 | -3.2% | $-89.17 | -1.9 | done | can't tell from luck |
| value_ev5 | 2421 | 40.5 | 41.1 | $-1192.22 | -4.9% | $-192.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2812 | 49.5 | 49.4 | $-1280.50 | -4.6% | $-280.50 | -2.4 | done | losing for real |
| trend_filter | 1983 | 48.8 | 50.5 | $-1670.71 | -8.4% | $-670.71 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2812 | 50.5 | 51.0 | $-1670.81 | -5.9% | $-670.81 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3361 | 49.2 | 50.2 | $-2070.86 | -6.2% | $-1070.86 | -3.6 | done | losing for real |
| coinflip | 4839 | 50.0 | 50.1 | $-2227.19 | -4.6% | $-1227.19 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4839 | 50.3 | 51.4 | $-2929.52 | -6.1% | $-1929.52 | -4.3 | done | losing for real |
| always_up | 4839 | 47.8 | 49.3 | $-3542.14 | -7.3% | $-2542.14 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7793 | 48.1 | 48.9 | $-4365.36 |
| ETH | 8418 | 48.1 | 48.3 | $-4933.97 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
