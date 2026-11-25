# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1346 windows, 35327 settled trades, 413 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 697 | 34.1 | 35.4 | $-558.07 | -8.0% | $441.93 | -1.6 | done | can't tell from luck |
| value_ev10 | 1703 | 38.8 | 39.2 | $-814.05 | -4.8% | $185.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3536 | 50.8 | 50.1 | $-1039.40 | -2.9% | $-39.40 | -1.7 | done | can't tell from luck |
| value_ev5 | 2571 | 40.5 | 41.1 | $-1321.12 | -5.1% | $-321.12 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2968 | 49.4 | 49.5 | $-1440.82 | -4.9% | $-440.82 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2968 | 50.6 | 50.9 | $-1573.36 | -5.3% | $-573.36 | -3.0 | done | losing for real |
| trend_filter | 2102 | 48.7 | 50.5 | $-1789.16 | -8.5% | $-789.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3536 | 49.2 | 50.3 | $-2207.68 | -6.2% | $-1207.68 | -3.8 | done | losing for real |
| coinflip | 5082 | 50.0 | 50.1 | $-2301.98 | -4.5% | $-1301.98 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5082 | 50.3 | 51.4 | $-3035.85 | -6.0% | $-2035.85 | -4.4 | done | losing for real |
| always_up | 5082 | 47.8 | 49.3 | $-3728.02 | -7.3% | $-2728.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8670 | 47.9 | 48.8 | $-5298.31 |
| ETH | 9347 | 48.2 | 48.2 | $-4926.98 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
