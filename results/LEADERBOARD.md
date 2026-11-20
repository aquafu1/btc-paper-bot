# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 948 windows, 26293 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 485 | 35.3 | 34.8 | $-134.35 | -2.8% | $865.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1193 | 38.2 | 39.1 | $-618.60 | -5.2% | $381.40 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2687 | 51.2 | 50.6 | $-808.83 | -3.0% | $191.17 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2251 | 50.2 | 49.7 | $-863.50 | -3.8% | $136.50 | -1.8 | done | can't tell from luck |
| trend_filter | 1569 | 50.0 | 50.8 | $-999.16 | -6.4% | $0.84 | -2.6 | done | losing for real |
| value_ev5 | 1812 | 40.0 | 41.0 | $-1002.38 | -5.5% | $-2.38 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 2251 | 49.8 | 51.0 | $-1622.79 | -7.2% | $-622.79 | -3.5 | done | losing for real |
| coinflip | 3786 | 50.3 | 50.4 | $-1648.63 | -4.4% | $-648.63 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2687 | 48.8 | 50.2 | $-1805.06 | -6.7% | $-805.06 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3786 | 51.0 | 51.5 | $-1852.37 | -4.9% | $-852.37 | -3.1 | done | losing for real |
| always_up | 3786 | 46.9 | 49.6 | $-3726.78 | -9.8% | $-2726.78 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5993 | 48.2 | 49.0 | $-3342.28 |
| ETH | 6539 | 48.2 | 48.5 | $-3945.53 |
| SOL | 6856 | 48.2 | 48.6 | $-3821.66 |
| XRP | 6905 | 48.3 | 48.5 | $-3973.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
