# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 565 windows, 15661 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1332 | 51.2 | 49.7 | $-274.55 | -2.1% | $725.45 | -0.8 | done | can't tell from luck |
| value_ev20 | 307 | 32.9 | 35.2 | $-365.92 | -11.9% | $634.08 | -1.6 | done | can't tell from luck |
| trend_filter | 909 | 50.4 | 51.1 | $-537.42 | -5.9% | $462.58 | -1.8 | done | can't tell from luck |
| value_ev10 | 744 | 37.4 | 39.4 | $-736.41 | -9.9% | $263.59 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1588 | 49.2 | 49.8 | $-879.74 | -5.5% | $120.26 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1588 | 50.8 | 51.1 | $-900.01 | -5.7% | $99.99 | -2.3 | done | losing for real |
| value_ev5 | 1105 | 39.5 | 41.3 | $-931.53 | -8.4% | $68.47 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1332 | 48.8 | 51.2 | $-1292.92 | -9.7% | $-292.92 | -3.6 | done | losing for real |
| coinflip | 2252 | 49.8 | 50.5 | $-1305.55 | -5.8% | $-305.55 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 2252 | 50.2 | 51.9 | $-1603.70 | -7.1% | $-603.70 | -3.5 | done | losing for real |
| always_up | 2252 | 47.2 | 49.9 | $-2246.60 | -10.0% | $-1246.60 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3541 | 47.6 | 49.2 | $-2754.06 |
| ETH | 3903 | 47.9 | 48.6 | $-2837.03 |
| SOL | 4087 | 47.8 | 48.7 | $-3100.60 |
| XRP | 4130 | 48.5 | 48.6 | $-2382.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
