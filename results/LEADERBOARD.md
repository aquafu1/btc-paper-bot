# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 301 windows, 8035 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 148 | 35.1 | 36.5 | $-134.69 | -9.1% | $865.31 | -0.9 | Sun 3:15 AM | too few trades (148/200) |
| reversal_15m_0.10pct | 799 | 53.1 | 51.9 | $-169.84 | -2.1% | $830.16 | -0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 653 | 52.7 | 51.9 | $-194.74 | -3.0% | $805.26 | -0.8 | done | can't tell from luck |
| value_ev10 | 384 | 38.3 | 40.5 | $-371.48 | -9.7% | $628.52 | -1.6 | done | can't tell from luck |
| value_ev5 | 568 | 40.0 | 42.2 | $-552.78 | -9.7% | $447.22 | -2.0 | done | losing for real |
| trend_filter | 443 | 46.0 | 50.2 | $-573.45 | -12.9% | $426.55 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 653 | 47.3 | 49.8 | $-644.60 | -9.9% | $355.40 | -2.6 | done | losing for real |
| coinflip | 1196 | 50.0 | 50.9 | $-719.62 | -6.0% | $280.38 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 799 | 46.9 | 49.9 | $-804.95 | -10.1% | $195.05 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1196 | 49.1 | 51.3 | $-1019.99 | -8.5% | $-19.99 | -3.1 | done | losing for real |
| always_up | 1196 | 47.2 | 50.3 | $-1228.30 | -10.3% | $-228.30 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1800 | 46.6 | 49.4 | $-1736.50 |
| ETH | 2013 | 47.0 | 48.8 | $-1890.38 |
| SOL | 2087 | 48.3 | 49.4 | $-1616.51 |
| XRP | 2135 | 48.7 | 49.1 | $-1171.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
