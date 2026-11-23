# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1219 windows, 33449 settled trades, 376 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1599 | 38.8 | 39.2 | $-760.67 | -4.8% | $239.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3352 | 50.8 | 50.3 | $-1089.37 | -3.2% | $-89.37 | -1.9 | done | can't tell from luck |
| value_ev5 | 2417 | 40.5 | 41.1 | $-1175.89 | -4.9% | $-175.89 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2807 | 49.5 | 49.4 | $-1281.91 | -4.6% | $-281.91 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2807 | 50.5 | 51.1 | $-1659.58 | -5.9% | $-659.58 | -3.2 | done | losing for real |
| trend_filter | 1979 | 48.7 | 50.4 | $-1682.12 | -8.5% | $-682.12 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3352 | 49.2 | 50.2 | $-2060.63 | -6.1% | $-1060.63 | -3.6 | done | losing for real |
| coinflip | 4828 | 50.0 | 50.1 | $-2215.40 | -4.6% | $-1215.40 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4828 | 50.2 | 51.4 | $-2940.13 | -6.1% | $-1940.13 | -4.4 | done | losing for real |
| always_up | 4828 | 47.8 | 49.3 | $-3529.10 | -7.3% | $-2529.10 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7761 | 48.1 | 48.9 | $-4342.06 |
| ETH | 8378 | 48.1 | 48.3 | $-4911.95 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
